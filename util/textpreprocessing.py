
def preprocess_text(text, pipeline):
    if len(pipeline)==0:
        return text
    else:
        return preprocess_text(pipeline[0](text), pipeline[1:])