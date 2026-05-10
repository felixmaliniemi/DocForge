from .java import analyze_java

def analyze_csharp(content):
    """Extraherar C#-klasser och metoder med regional analys 
       baserat på klammerpar (speglar Java-logiken)"""
    return analyze_java(content)
