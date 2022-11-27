from modelapi.models import model

def predict(X, model):
    return model.predict(X)[0]

def get_parsed_prediction(input):
    prediction = predict(input, model)

    if prediction == 1:
        label = "IrisVirginica"
    elif prediction == 2:
        label = "IrisVersicolour"
    else:
        label ="IrisSetosa"
        
    return {"label": label, "prediction": int(prediction)}