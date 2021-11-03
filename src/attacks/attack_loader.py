from secml.adv.attacks import CFoolboxPGDLinf, CFoolboxFGM

from src.attacks.autoattack_wrapper import CAutoAttackAPGDCE, CAutoAttackAPGDDLR
from src.attacks.autoattack_wrapper.wrapper.autoattack_apgd_attack import CAutoAttackAPGDDLRAdaptive
from src.attacks.pgd_adaptive import CFoolboxPGDLinfAdaptive
from src.attacks.pgd_logits import CFoolboxLogitsPGD
from src.attacks.smoothed_pgd import CFoolboxAveragedPGD
from src.models.model_loader import check_model_id, load_model

ORIGINAL_ATTACKS = {
    0: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 0,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 5,
    },

    1: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 1,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.3,
            "abs_stepsize": 0.1,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 5,
    },

    2: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 2,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.01,
            "abs_stepsize": 0.001,
            "random_start": False,
            "steps": 10
        },
        "random_restarts": 5,
    },

    3: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 4,
        "transfer": 3,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 2,
    },
    5: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 5,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.00155,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },
    6: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 6,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 1.0,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },
    7: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 7,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 1.0,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },
    8: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 8,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.0078,
            "random_start": False,
            "steps": 20
        },
        "random_restarts": 10,
    },
    9: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 9,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.0078,
            "random_start": False,
            "steps": 20
        },
        "random_restarts": 5,
    },
    10: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 10,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.003,
            "random_start": False,
            "steps": 20
        },
        "random_restarts": 0,
    },
    11: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 11,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.003,
            "random_start": False,
            "steps": 20
        },
        "random_restarts": 0,
    },
    12: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 12,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.007,
            "random_start": False,
            "steps": 20
        },
        "random_restarts": 0,
    },
    13: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 13,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.0078,
            "random_start": False,
            "steps": 100
        },
        "random_restarts": 3,
    },
    14: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 14,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.0078,
            "random_start": False,
            "steps": 20
        },
        "random_restarts": 0,
    },
    15: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 15,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.0078,
            "random_start": False,
            "steps": 20
        },
        "random_restarts": 0,
    },
    16: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 16,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.375,
            "random_start": False,
            "steps": 20
        },
        "random_restarts": 0,
    },
    17: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 17,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 40
        },
        "random_restarts": 0,
    },
}

ADAPTIVE_ATTACKS = {
    0: {
        "attack": "CFoolboxAveragedPGD",
        "model_id": 0,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.003,
            "random_start": False,
            "steps": 50,
            "k": 200,
            "sigma": 0.031
        },
        "random_restarts": 1
    },

    1: {
        "attack": "CFoolboxLogitsPGD",
        "model_id": 1,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.3,
            "abs_stepsize": 0.1,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },

    2: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 2,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.01,
            "abs_stepsize": 0.003,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 3,
    },

    3: {
        "attack": "CFoolboxPGDLinfAdaptive",
        "model_id": 3,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 2,
    },
    5: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 5,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },
    6: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 6,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },
    7: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 7,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 5,
    },
    8: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 8,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 5,
    },
    9: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 9,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 5,
    },
    10: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 10,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 40
        },
        "random_restarts": 3,
    },
    11: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 11,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 40
        },
        "random_restarts": 3,
    },
    12: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 12,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },
    13: {
        "attack": "CFoolboxAveragedPGD",
        "model_id": 13,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.0078,
            "random_start": False,
            "steps": 50,
            "k": 30,
            "sigma": 0.031
        },
        "random_restarts": 3
    },
    14: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 14,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },
    15: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 15,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 10,
    },
    16: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 16,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.03,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 5,
    },
    17: {
        "attack": "CFoolboxPGDLinf",
        "model_id": 17,
        "attack_params": {
            "y_target": None,
            "epsilons": 0.031,
            "abs_stepsize": 0.01,
            "random_start": False,
            "steps": 50
        },
        "random_restarts": 5,
    },

}

AUTO_PGD_ATTACKS = {
    0: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 0,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"}
    },
    1: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 1,
        "attack_params": {
            "dmax": 0.3,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    2:
        {
            "attack": "CAutoAttackAPGDDLR",
            "model_id": 2,
            "attack_params": {
                "dmax": 0.031,
                "y_target": None,
                "epsilons": False,
                "version": "plus",
            }
        },
    3: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 4,
        "transfer": 3,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    5: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 5,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    6: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 6,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    7: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 7,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    8: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 8,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    9: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 9,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    10: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 10,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    11: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 11,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    12: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 12,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    13: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 13,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    14: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 14,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    15: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 15,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    16: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 16,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
    17: {
        "attack": "CAutoAttackAPGDDLR",
        "model_id": 17,
        "attack_params": {
            "dmax": 0.031,
            "y_target": None,
            "epsilons": False,
            "version": "plus"
        }
    },
}

ATTACK_CLASSES = {
    'CFoolboxPGDLinf': CFoolboxPGDLinf,
    'CFoolboxFGSM': CFoolboxFGM,
    'CFoolboxAveragedPGD': CFoolboxAveragedPGD,
    'CFoolboxLogitsPGD': CFoolboxLogitsPGD,
    'CFoolboxPGDLinfAdaptive': CFoolboxPGDLinfAdaptive,
    'CAutoAttackAPGDCE': CAutoAttackAPGDCE,
    'CAutoAttackAPGDDLR': CAutoAttackAPGDDLR,
    'CAutoAttackAPGDDLRAdaptive': CAutoAttackAPGDDLRAdaptive,
}


def _load_attack(model_id, attack_dict):
    check_model_id(model_id)
    attack_cls = ATTACK_CLASSES[attack_dict[model_id]['attack']]
    model = load_model(attack_dict[model_id]['model_id'])
    attack_args = attack_dict[model_id]['attack_params']
    attack = attack_cls(model, **attack_args)
    if "transfer" in attack_dict[model_id]:
        model_transfer = load_model(attack_dict[model_id]['transfer'])
    else:
        model_transfer = model
    if "random_restarts" in attack_dict[model_id]:
        n_restarts = attack_dict[model_id]['random_restarts']
    else:
        n_restarts = 0
    return attack, model, model_transfer, n_restarts


def load_attack(model_id: int):
    return _load_attack(model_id, ORIGINAL_ATTACKS)


def load_mitigated_attack(model_id: int):
    return _load_attack(model_id, ADAPTIVE_ATTACKS)


def load_auto_attack(model_id: int):
    return _load_attack(model_id, AUTO_PGD_ATTACKS)
