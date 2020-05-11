import boto3
translate = boto3.client("translate")

def handler(request):
    try:
        data = translate.translate_text(
            SourceLanguageCode="auto",
            TargetLanguageCode="en",
            Text="Hola"
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return "Successfully executed"
