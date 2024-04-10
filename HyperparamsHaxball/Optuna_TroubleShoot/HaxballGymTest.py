import optuna

def objective(trial):
    x = trial.suggest_float('x', -10, 10)
    return (x - 2) ** 2

study = optuna.create_study(direction='minimize', study_name='simple_study', storage='sqlite:///simple_study.db')
study.optimize(objective, n_trials=10)

#the best trial
print(study.best_trial)
