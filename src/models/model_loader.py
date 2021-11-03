from src.models.cui_learnable import load_cui
from src.models.ding_mma import load_ding_mma
from src.models.distillation import load_distillation
from src.models.engstrom_robustness import load_engstrom_robustness
from src.models.ensemble_diversity import load_ensemble
from src.models.hendrycks_using import load_hendrycks_using
from src.models.huang_self import load_huang_self
from src.models.kwta import load_kwta
from src.models.pang_boosting import load_pang_boosting
from src.models.wu_adversarial import load_wu_adversarial
from src.models.sitawarin import load_sitawarin
from src.models.tws import load_tws
from src.models.hydra import load_hydra
from src.models.wong_fast import load_wong_fast
from src.models.zhang_geometry import load_zhang_geometry
from src.models.zhang_you import load_zhang_you
from src.models.zhang_theoretically import load_zhang_theoretically

MODELS = {
    0: load_kwta.load_model,
    1: load_distillation.load_model,
    2: load_ensemble.load_model,
    3: load_tws.load_model,
    4: load_tws.load_model_no_reject,
    5: load_hydra.load_model,
    6: load_wong_fast.load_model,
    7: load_pang_boosting.load_model,
    8: load_zhang_you.load_model,
    9: load_sitawarin.load_model,
    10: load_cui.load_model,
    11: load_zhang_theoretically.load_model,
    12: load_huang_self.load_model,
    13: load_ding_mma.load_model,
    14: load_hendrycks_using.load_model,
    15: load_wu_adversarial.load_model,
    16: load_engstrom_robustness.load_model,
    17: load_zhang_geometry.load_model,
}


def load_model(model_id: int):
    check_model_id(model_id)
    model = MODELS[model_id]()
    return model


def check_model_id(model_id):
    if model_id < 0 or model_id > len(MODELS):
        raise ValueError(f'{model_id} not in the range of provided model. Use 0,1,2,3 or 4')
