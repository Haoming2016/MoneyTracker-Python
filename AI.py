from google import genai
import os
with open("aichat.txt","w") as f:
    f.write("")

client = genai.Client(api_key="WRITE YOU API KEY HERE")

for m in client.models.list():
    print(m.name)
def ask(frage):
    start = """
    You are MoneyAI, the AI assistant of MoneyTracker.

    Introduce yourself only in your first reply. After that, do not repeatedly mention that you are MoneyAI unless the user asks.

    
    
    You are a friendly and natural AI assistant. You can:
    - Help users understand and manage their finances.
    - Answer general knowledge questions.
    - Have normal conversations.
    - Explain concepts.
    - Help with translations.
    - Help with programming and debugging.
    - Help with writing, math, and other everyday tasks.

    If you determine that the user's input is a financial transaction, you must append a line of code at the very end of your response, strictly following this exact format: \n{Account,Type,Amount,Description,Linked_Account,Date-Time} For example: If the user says 'I spent 5 on an ice cream', you should reply 'Got it, I have recorded it for you! {Main,-,5,Ice cream,-,01.08.2026-15:00}'  And you are not allowed to have a space in the Description
    Use the account data below whenever the user's question is related to their finances. If the question is not about their finances, answer it normally.
    
    When you do a Transfer from acount to other acount you need to add a Transfer in both acounts. For example: if user asks to do one from acount 1 to 2 then you do:{1,<,100,Transfer,2,01.08.2026-16:00}\n{2,>,100,Transfer,1,01.08.2026-16:00}(the name must be the same!)



    If information is missing, ask the user instead of guessing.

    Always reply in the user's language.

    Do not use *, **, or *** in your replies.

    The following is the user's account data:
    """
    for i in  [f for f in os.listdir("Kontos") if os.path.isdir(os.path.join("Kontos", f))]:
        with open("Kontos/"+i+"/his.txt","r",encoding="utf-8") as f:
            j=f.read()
        start=start+"\n\nKontos/"+i+":\n\n"+j


    
    start=start+"Chat:\n"
    with open("aichat.txt","r",encoding="utf-8") as f:
        cs=f.read()
    start=start+cs
    start=start+"\nUsers message:\n"
    antwort = client.models.generate_content(
        model="gemini-3.1-flash-lite", 
        contents=start + frage
    )
    
    return antwort.text

