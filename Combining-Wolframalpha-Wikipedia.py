import wx,wikipedia,wolframalpha
from espeak import espeak
import speech_recognition as sr

espeak.synth("Welcome")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450,100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | 
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am PyDa the Python Digital Assistant. How can I help you?"   )
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        if input == '':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
                try:
                    self.txt.SetValue(r.recognize_google(audio))
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
                try:
                    #wolframaplha
                    app_id = "YRG747-JJPR67VTA7"
                    client = wolframalpha.Client(app_id)

                    res = client.query(input)
                    answer = next(res.results).text

                    print answer
                    espeak.synth("The answer is " + answer)

                except:
                    #wikipedia
                    input = input.split(' ')
                    input = " ".join(input[2:])
                    wikipedia.set_lang("en")
                    espeak.synth("Searched for" + input)
                    print wikipedia.summary(input, sentences = 2)
                

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()


    