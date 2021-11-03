from robustbench import load_model as load
from secml.array import CArray
from secml.ml import CClassifierPyTorch


def load_model():
    model = load(model_name='Hendrycks2019Using', dataset='cifar10', threat_model='Linf')
    model = CClassifierPyTorch(model, input_shape=(3, 32, 32), pretrained=True,
                               pretrained_classes=CArray(list(range(10))), preprocess=None)
    return model