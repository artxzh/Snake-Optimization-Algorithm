import argparse
import json
import random
from pathlib import Path

import numpy as np
import optuna

from algorithms.fitness import evaluate_group
from algorithms.snake_optimizer import snake_optimizer
from problems.objective import sphere


def positive_int(value):
    parsed_value = int(value)
    if parsed_value <= 0:
        raise argparse.ArgumentTypeError("value must be a positive integer")
    return parsed_value


def even_population_size(value):
    parsed_value = positive_int(value)
    if parsed_value < 2 or parsed_value % 2 != 0:
        raise argparse.ArgumentTypeError(
            "population size must be an even integer greater than or equal to 2"
        )
    return parsed_value


def parse_args():
    parser = argparse.ArgumentParser(
        description="Tune the snake optimizer coefficients with Optuna."
    )
    parser.add_argument("--trials", type=positive_int, default=30)
    parser.add_argument("--dimensions", type=positive_int, default=5)
    parser.add_argument("--max-iterations", type=positive_int, default=100)
    parser.add_argument("--population-size", type=even_population_size, default=50)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/optuna_best_params.json"),
        help="Path where the best parameters are saved.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    lower_bound = np.full(args.dimensions, -1.0)
    upper_bound = np.full(args.dimensions, 1.0)

    def objective(trial):
        parameters = {
            "c1": trial.suggest_float("c1", 0.1, 1.0),
            "c2": trial.suggest_float("c2", 0.0001, 0.1, log=True),
            "c3": trial.suggest_float("c3", 0.1, 1.0),
        }

        trial_seed = args.seed + trial.number
        np.random.seed(trial_seed)
        random.seed(trial_seed)

        population = snake_optimizer(
            args.population_size,
            lower_bound,
            upper_bound,
            args.max_iterations,
            0,
            args.dimensions,
            sphere,
            **parameters,
        )
        return float(np.min(evaluate_group(population, sphere)))

    sampler = optuna.samplers.TPESampler(seed=args.seed)
    study = optuna.create_study(direction="minimize", sampler=sampler)
    study.enqueue_trial({"c1": 0.5, "c2": 0.005, "c3": 0.7})
    study.optimize(objective, n_trials=args.trials)

    result = {
        "objective": "sphere",
        "best_value": study.best_value,
        "best_parameters": study.best_params,
        "trials": args.trials,
        "seed": args.seed,
        "dimensions": args.dimensions,
        "max_iterations": args.max_iterations,
        "population_size": args.population_size,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as output_file:
        json.dump(result, output_file, indent=2)
        output_file.write("\n")

    print(f"Melhor valor da função Sphere: {study.best_value:.8f}")
    print("Melhores parâmetros:")
    for name, value in study.best_params.items():
        print(f"  {name}: {value:.8f}")
    print(f"Resultado salvo em: {args.output}")


if __name__ == "__main__":
    main()
