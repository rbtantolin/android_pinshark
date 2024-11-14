from py3pin.Pinterest import Pinterest
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timezone
from random import randint
from time import sleep
from tqdm import tqdm
import json
import os
import colorama
from colorama import Fore, Style
import time
import datetime
from datetime import datetime

global pinterest
os.system(f'mode con: cols={76}')
print(Fore.RED + '')
print(''' .S_sSSs    .S  .S_sSSs     sSSs  .S   S.   .SSSSs    .S_sSSs    .S    S.   
.SS~YS%%b  .SS .SS~YS%%b   d%%SP .SS   SS. .SSSSSSS  .SS~YS%%b  .SS    SS.  
S%S   `S%b S%S S%S   `S%b d%S'   S%S   S%S S%S  SSSS S%S   `S%b S%S    S&S  
S%S    S%S S%S S%S    S%S S%|    S%S   S%S S%S   S%S S%S    S%S S%S    d*S  
S%S    d*S S&S S%S    S&S S&S    S%SSSSS%S S%SSSSS%S S%S    d*S S&S   .S*S  
S&S   .S*S S&S S&S    S&S Y&Ss   S&S SSS&S S&S SSS%S S&S   .S*S S&S_sdSSS   
S&S_sdSSS  S&S S&S    S&S `S&&S  S&S   S&S S&S   S&S S&S_sdSSS  S&S~YSSY%b  
S&S~YSSY   S&S S&S    S&S   `S*S S&S   S&S S&S   S&S S&S~YSY%b  S&S    `S%  
S*S        S*S S*S    S*S    l*S S*S   S*S S*S   S&S S*S   `S%b S*S     S%  
S*S        S*S S*S    S*S   .S*P S*S   S*S S*S   S*S S*S    S%S S*S     S&  
S*S        S*S S*S    S*S sSS*S  S*S   S*S S*S   S*S S*S    S&S S*S     S&  
S*S        S*S S*S    SSS YSS'   SSS   S*S SSS   S*S S*S    SSS S*S     SS  
SP         SP  SP                      SP        SP  SP         SP          
Y          Y   Y                       Y         Y   Y          Y           
==================================v1.672==================================
''')

print(Fore.GREEN + '')

# print("""
# Availabel User:
# 1. anthonyberlins
# 2. arsanashop
# GRUP 1
# 3. anthonysaviore
# 4. el_utheromania
# 5. seivonix
# 6. graphicartxelo
# GRUP 2
# 7. blazens601
# 8. kazzekazze
# 9. xelographic
# 10. ws190474
# GRUP3
# 11. baddieszone
# 12. armyisarmy
# 13. BerryPOPAesthetic
# 14. leasummerell
# GRUP 4
# 15. ortmelin
# 16. gnavelic
# 17. ansorymurcus
# 18. abmuxxx

# 19. plantgardenia
# 00. no user          
#           """)


countrSkip = 0
countrDnld = 0  

# user_data = [
#     {'number': 1, 'username':'anthonyberlins', 'password':'musicmania1', 'email':'hawanaworld@gmail.com'},
#     {'number': 2, 'username':'arsanashop', 'password':'musicmania1', 'email':'arsana.shop@gmail.com'},
#     {'number': 3, 'username':'anthonysaviore', 'password':'musicmania1', 'email':'baxxiro@gmail.com'},
#     {'number': 4, 'username':'el_utheromania', 'password':'musicmania1', 'email':'iqbal.arsana@gmail.com'},
#     {'number': 5, 'username':'seivonix', 'password':'musicmania1', 'email':'sulrahmat01@gmail.com'},
#     {'number': 6, 'username':'graphicartxelo', 'password':'musicmania1', 'email':'jorzbob@gmail.com'},
#     {'number': 7, 'username':'blazens601', 'password':'musicmania1', 'email':'iqbaldf.arsanatnt@gmail.com'},
#     {'number': 8, 'username':'kazzekazze', 'password':'musicmania1!', 'email':'ashanoon1009@gmail.com'},
#     {'number': 9, 'username':'xelographic', 'password':'musicmania1', 'email':'xelo.graphic@gmail.com'},
#     {'number': 10, 'username':'ws190474', 'password':'musicmania1', 'email':'ws190474@gmail.com'},
#     {'number': 11, 'username':'baddieszone', 'password':'candychooper', 'email':'hapsarihani02@gmail.com'},
#     {'number': 12, 'username':'armyisarmy', 'password':'musicmania1!!', 'email':'melaniezara346@gmail.com'},
#     {'number': 13, 'username':'BerryPOPAesthetic', 'password':'musicmania1!', 'email':'arsana.tnt@gmail.com'},
#     {'number': 14, 'username':'leasummerell', 'password':'musicmania1', 'email':'leasummerell@gmail.com'},
#     {'number': 15, 'username':'ortmelin', 'password':'musicmania1', 'email':'theresiaortmelin@gmail.com'},
#     {'number': 16, 'username':'gnavelic', 'password':'musicmania1', 'email':'sparkgretha@gmail.com'},
#     {'number': 17, 'username':'ansorymurcus', 'password':'musicmania1', 'email':'tukkuwo@gmail.com'},
#     {'number': 18, 'username':'abmuxxx', 'password':'musicmania1', 'email':'mukarimabdul81@gmail.com'},
#     {'number': 19, 'username':'plantgardenia', 'password':'candychooper1', 'email':'plantgardenia88@gmail.com'},
#     {'number': 00, 'username':'username', 'password':'password', 'email':'email'},
# ]

import json
import os

def manage_login_data(file_path='login_data.txt'):
    def load_login_data():
        # Memeriksa keberadaan file dan memuat data jika ada
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Format file tidak valid.")
                    return []
        return []

    def save_login_data(data):
        # Menyimpan data login ke file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def display_logins(data):
        # Menampilkan daftar username dan nomor urut
        print("Daftar Login:")
        for login in data:
            print(f"{login['number']}: {login['username']}")

    def add_login(data):
        # Menambahkan login baru
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        email = input("Masukkan email: ")
        new_login = {
            "number": len(data) + 1,
            "username": username,
            "password": password,
            "email": email
        }
        data.append(new_login)
        save_login_data(data)
        print("Data login berhasil ditambahkan.")
        
    def edit_login(data):
        # Mengedit data login
        try:
            number = int(input("Masukkan nomor akun yang ingin diedit: "))
            for login in data:
                if login['number'] == number:
                    login['username'] = input("Masukkan username baru: ") or login['username']
                    login['password'] = input("Masukkan password baru: ") or login['password']
                    login['email'] = input("Masukkan email baru: ") or login['email']
                    save_login_data(data)
                    print("Data login berhasil diperbarui.")
                    return
            print("Data login tidak ditemukan.")
        except ValueError:
            print("Input tidak valid.")

    def delete_login(data):
        # Menghapus data login
        try:
            number = int(input("Masukkan nomor akun yang ingin dihapus: "))
            data[:] = [login for login in data if login['number'] != number]
            # Update nomor urut setelah penghapusan
            for i, login in enumerate(data):
                login['number'] = i + 1
            save_login_data(data)
            print("Data login berhasil dihapus.")
        except ValueError:
            print("Input tidak valid.")

    # Memuat data login dari file
    login_data = load_login_data()

    while True:
        # Menampilkan daftar login saat program dimulai
        if login_data:
            display_logins(login_data)
        else:
            print("Tidak ada data login. Silakan tambah data login.")

        # Menampilkan opsi menu
        print("\nPilihan:")
        print("1. Pilih login")
        print("2. Tambah login")
        print("3. Edit login")
        print("4. Hapus login")
        print("5. Keluar")

        choice = input("Masukkan pilihan Anda: ")
        
        if choice == '1' and login_data:
            try:
                selection = int(input("Pilih nomor akun yang ingin Anda gunakan: "))
                selected_login = next((login for login in login_data if login['number'] == selection), None)
                if selected_login:
                    Pinterest(email=selected_login['email'], password=selected_login['password'], username=selected_login['username'], cred_root='cred_root')
                    return pinterest
                else:
                    print("Nomor akun tidak valid.")
            except ValueError:
                print("Input tidak valid.")
        
        elif choice == '2':
            add_login(login_data)
        
        elif choice == '3' and login_data:
            edit_login(login_data)
        
        elif choice == '4' and login_data:
            delete_login(login_data)
        
        elif choice == '5':
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# def get_credentials(data, number):
#     for entry in data:
#         if entry.get('number') == number:
#             return entry.get('username'), entry.get('password'), entry.get('email')
#     return None

# def user_account():
#     result = get_credentials(user_data, int(input('Account Number: ')))
#     proxies = {"http":"http://Seljossbossoke:C7w5RjK@161.77.171.162:50101"}
    
#     if result:
#         username, password, email = result
#         print(username)
#     else:
#         print('Credentials not found for the given number.')
        
    # return Pinterest(email=email, password=password, username=username, cred_root='cred_root', proxies=proxies)
    
def process_and_sort_pins(pinterest, data):
    sorted_pins = []
    min_saves = int(input('Min Saves Count: '))
    top_n_sort = input('Ingin di-sort berdasarkan Saves teratas? (y/n): ').strip().lower()
    
    # Jika user memilih sorting, tanyakan jumlah n teratas
    if top_n_sort == 'y':
        try:
            top_n = int(input('Jumlah data teratas yang ingin ditampilkan: '))
        except ValueError:
            print("Input tidak valid. Menampilkan semua data yang memenuhi kriteria min_saves.")
            top_n = None
    else:
        top_n = None  # Jika tidak ingin sort, top_n diatur None
        
    for pin_id in tqdm(data):
        pin_data = {}
        
        # Mulai proses pengambilan dan pemilahan data
        try:
            # Ambil info pin dari Pinterest
            info = pinterest.load_pin(pin_id=pin_id['id'])
            # Hitung umur pin (dalam hari)
            created_at_str = info.get('createdAt', None)
            if created_at_str:
                created_at = datetime.strptime(created_at_str, "%a, %d %b %Y %H:%M:%S %z")
                now = datetime.now(timezone.utc)
                days_difference = (now - created_at).days
            else:
                days_difference = 'Null'

            # Data user original dan pinner
            ori_username = info.get('nativeCreator', {}).get('username', None)
            pinner_username = info.get('pinner', {}).get('username', None)
            user_info_ori = pinterest.get_user_overview(username=ori_username) if ori_username else {}
            user_info_pinner = pinterest.get_user_overview(username=pinner_username) if pinner_username else {}

            # Simpan data pin dalam dictionary
            pin_data['Pin ID'] = info.get('entityId', 'Null')
            saves = info.get('aggregatedPinData', {}).get('aggregatedStats', {}).get('saves', 'Null')
            if saves != 'Null' and saves is not None:
                try:
                    saves = int(saves)
                except ValueError:
                    saves = 0
            pin_data['Saves'] = saves
            pin_data['Repin'] = info.get('repinCount', 0)
            pin_data['Ori Pinner'] = ori_username if ori_username else 'Null'
            pin_data['Follower Count (Ori)'] = info.get('nativeCreator', {}).get('followerCount', 'Null')
            pin_data['Ori Visit'] = user_info_ori.get('profile_views', 'Null')
            pin_data['Pinner'] = pinner_username if pinner_username else 'Null'
            pin_data['Follower Count (Pinner)'] = info.get('pinner', {}).get('followerCount', 'Null')
            pin_data['Visit'] = user_info_pinner.get('profile_views', 'Null')
            pin_data['Age'] = days_difference

            # Proses hashtags jika ada
            visual_annotation = info.get('pinJoin', {}).get('visualAnnotation', None)
            pin_data['Hashtags'] = ', '.join(tag.strip('#') for tag in visual_annotation) if visual_annotation else 'Null'

            # Memeriksa apakah jumlah `saves` memenuhi standar minimum
            saves = pin_data['Saves']
            if saves != 'Null' and saves >= min_saves:
                sorted_pins.append(pin_data)
        
        except Exception as e:
            pass

    if top_n_sort == 'y' and top_n is not None:
        sorted_pins = sorted(sorted_pins, key=lambda x: x['Saves'], reverse=True)[:top_n]
    
    for pin in sorted_pins:
        keys = list(pin.keys())
        selected_keys = [keys[0], keys[1]]
        for key in selected_keys:
            print(f"{key}: {pin[key]}")


def info_pin():
    pin_data = {}
    pin_id = input('Pin ID: ')
    info = pinterest.load_pin(pin_id=pin_id)
    try:
        # Hitung umur pin (dalam hari)
        created_at_str = info.get('createdAt', None)
        if created_at_str:
            created_at = datetime.strptime(created_at_str, "%a, %d %b %Y %H:%M:%S %z")
            now = datetime.now(timezone.utc)
            days_difference = (now - created_at).days
        else:
            days_difference = 'Null'

        # Data user original dan pinner
        ori_username = info.get('nativeCreator', {}).get('username', None)
        pinner_username = info.get('pinner', {}).get('username', None)
        user_info_ori = pinterest.get_user_overview(username=ori_username) if ori_username else {}
        user_info_pinner = pinterest.get_user_overview(username=pinner_username) if pinner_username else {}

        # Simpan data pin dalam dictionary
        pin_data['Pin ID'] = info.get('entityId', 'Null')
        pin_data['Saves'] = info.get('aggregatedPinData', {}).get('aggregatedStats', {}).get('saves', 'Null')
        pin_data['Repin'] = info.get('repinCount', 0)
        pin_data['Ori Pinner'] = ori_username if ori_username else 'Null'
        pin_data['Follower Count (Ori)'] = info.get('nativeCreator', {}).get('followerCount', 'Null')
        pin_data['Ori Visit'] = user_info_ori.get('profile_views', 'Null')
        pin_data['Pinner'] = pinner_username if pinner_username else 'Null'
        pin_data['Follower Count (Pinner)'] = info.get('pinner', {}).get('followerCount', 'Null')
        pin_data['Visit'] = user_info_pinner.get('profile_views', 'Null')
        pin_data['Age'] = days_difference

        # Proses hashtags jika ada
        visual_annotation = info.get('pinJoin', {}).get('visualAnnotation', None)
        pin_data['Hashtags'] = ', '.join(tag.strip('#') for tag in visual_annotation) if visual_annotation else 'Null'

    except Exception as e:
        print(f"Error processing pin {pin_id}: {e}")

                
    print(f"""
          Pin ID    = {pin_data['Pin ID']}
          Saves     = {pin_data['Saves']}
          Repin     = {pin_data['Repin']}
          Author    = {pin_data['Ori Pinner']}
          A.Follower= {pin_data['Follower Count (Ori)']}
          A.Visitor = {pin_data['Ori Visit']}
          Repinner  = {pin_data['Pinner']}
          R.Follower= {pin_data['Follower Count (Pinner)']}
          R.Visitor = {pin_data['Visit']}
          Pin Age   = {pin_data['Age']}
          Hashtag   = {pin_data['Hashtags']}
          """)
    # print(pin_data)

def info_board_feed(pinterest):
    result=pinterest.board_feed(board_id=input('Board ID: '))
    board_feed_data = process_and_sort_pins(data=result) 
    
    return board_feed_data

# def board_feed_excel():
#     save_excel(targeted_pins=info_board_feed(pinterest=pinterest))
    
def download_image(url, path):
    global countrSkip
    global countrDnld
    if os.path.isfile(path):
        countrSkip += 1
    else:
        nb_tries = 10
        while True:
            nb_tries -= 1
            try:
                r = requests.get(url=url, stream=True)
                break
            except ConnectionError as err:
                if nb_tries == 0:
                    raise err
                else:
                    time.sleep(1)
        if r.status_code == 200:
            countrDnld += 1
            # print("Downloading " + url)
            with open(path, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)

# def open_file_excel():
#     file_path = filedialog.askopenfilename(
#         title="Select a file",
#         filetypes=[("Text files", "*.xlsx"),
#                    ("All files", "*.*")]
#         )

#     return file_path

# def save_excel(targeted_pins):
#     save_path = filedialog.asksaveasfilename(
#         defaultextension='.xlsx', 
#         initialfile = ''
#         )
    
#     pd.DataFrame(targeted_pins).to_excel(save_path, index=False)
    
#     print(f'{len(targeted_pins)} pins saved')

def info_pin_search(pinterest):
    result=pinterest.search(scope='pins', query=input('Search Query: '))
    search_pins = process_and_sort_pins(data=result)
           
    return search_pins


# def info_pin_excel():
#     print('Excel file reading')
#     excel_pins = []
    
#     dtxl = pd.read_excel(
#         open_file_excel(), 
#         sheet_name='Sheet1', 
#         dtype=str
#         )
    
#     for x in tqdm(dtxl['Pin ID']):
#         excel_pins.append(data_pin(pin_id=x))
    
#     return excel_pins
    
def single_repin(pinterest):
    pinterest.repin(pin_id=input('Pin ID: '), board_id=input('Board ID: '))
        
# def image_download():
    
#     path_folder = filedialog.askdirectory()
    
#     if not os.path.exists(path_folder):
#         os.makedirs(path_folder)
        
#     print(f'Save to: {path_folder}')
    
    
#     while True:
#         method = int(input('Download image from - 1)Search 2)Board 3)Excel : '))
        
#         if method == 1:
#             pins = info_pin_search(pinterest)
#             break
        
#         elif method == 2:
#             pins = info_board_feed(pinterest)
#             print(pins)
#             break
        
#         elif method ==3:
            
#             file_path = filedialog.askopenfilename()
#             pins = pd.read_excel(file_path, sheet_name='Sheet1', dtype=str).to_dict(orient='records')
                        
#             break
        
#         else:
#             print('Wrong Number. Try Again')
#             pass
    
#     print('Start to download images')
#     for pin in tqdm(pins):
#         try:
#             info = pinterest.load_pin(pin_id=pin['Pin ID'])
#             url = info['images']['orig']['url']
            
#             download_image(url, path_folder + '/' + pin['Pin ID'] + '.' + url.rsplit('/' and '.', 1)[-1])
        
#         except (TypeError, IndexError) as e:
#             pass
    
#     print("Existing files:" + str(countrSkip))
#     print("New files:" + str(countrDnld))    

# def comment(pinterest=pinterest):
#     comment_mode = int(input('Comment Based: 1)Homefeed 2)Search 3)Excel: '))
#     if comment_mode == 1:
#         pins = sort_pin(result=pinterest.home_feed(), std=int(input('STD: ')))
                 
#     elif comment_mode == 2:
#         pins = sort_pin(result=pinterest.search(scope='pins', query=input('Search query: ')), std=int(input('STD: ')))
        
#     elif comment_mode == 3:
#         file_path = filedialog.askopenfilename()
#         pins = pd.read_excel(file_path, sheet_name='Sheet1', dtype=str).to_dict(orient='records')
    
#     file_path = filedialog.askopenfilename()
#     for x in pins:
#         df = pd.read_excel(file_path)
#         unique_values = df.stack().unique()
#         try:
#             if len(unique_values) == 0:
#                 print("All values have been used.")
#             else:
#                 random_value = random.choice(unique_values)
#                 pinterest.comment(pin_id=x['Pin ID'], text=random_value)
#                 print(f"{random_value} commented at {x['Pin ID']}")
#             sleep(randint(50,100))
#         except Exception as e:
#             print(e)
#             pass

def board_recommend(pinterest):
    print('Check Recommendation')
    result=pinterest.board_recommendations(board_id=input('Board ID: '), page_size=int(input('Page Size(Max 200): ')))
    
    
#     save_excel(targeted_pins=pins)
def all_board_info():
    username = input('Target Username: ')
    boards = pinterest.boards_all(username=username)
    for board in boards:
        print(f"Board ID: {board['id']}  {board['name']}")
        try:
            sections = pinterest.get_board_sections(board_id=board['id'])
            for section in sections:
                print(len(board['id'])*' ' + f"{section['id']} {(section['slug'])}")
        except:
            pass


# def upload_pin_direct(pinterest):
#     folder_target = filedialog.askopenfilenames(filetypes=[("Image Files", ".jpg .png")])
    
#     print("Start to upload")
#     for x in tqdm(folder_target):
#         sleep(randint(5,10))
#         pinterest.upload_pin(
#             board_id=input('Board ID Destination: '),
#             image_file=x,
#             description=None,
#             title=None,
#             section_id=None,
#             link=None
#             )

# def built_upload_excel():
#     data = []
    
#     for images in tqdm(filedialog.askopenfilenames(filetypes=[("Image Files", ".jpg .png")])):
#         data.append(images)
    
#     if len(data) > 0:
#         address = {
#             'Image Address' : data,
#             'Title' : None,
#             'Description' : None,
#             'Link' : None
#             }
#         pd.DataFrame(address).to_excel(
#             filedialog.asksaveasfilename(
#             filetypes=[("Excel Files", ".xlsx")], 
#             defaultextension='.xlsx'
#             )
#             )
#     print(Fore.LIGHTGREEN_EX + 'Built complete. Check the file in your directory')

# def upload_pin_excel(pinterest):
#     results = pd.read_excel(filedialog.askopenfilename(filetypes=[("Excel Files", ".xlsx")]), 
#             sheet_name='Sheet1', dtype=str).to_dict('records')
    
#     print(f"Open excel file with {len(results)} ID ready to pin")
#     board_id = input('Board ID Destination: ')
#     upload = int(input('1.Complete 2.Nolink 3.OnlyPic 4.Link: '))
#     start = int(input('Start Point:'))
#     stop = int(input('Stop Point:'))
           
#     upload_options = {
#     1: {"description": lambda x: x['Description'], "title": lambda x: x['Title'], "link": lambda x: x['Link']},
#     2: {"description": lambda x: x['Description'], "title": lambda x: x['Title'], "link": lambda x: None},
#     3: {"description": lambda x: None, "title": lambda x: x['Title'], "link": lambda x: None},
#     4: {"description": lambda x: None, "title": lambda x: None, "link": lambda x: x['Link']}
# }

# # Loop untuk upload pin
#     for x in tqdm(results[start:stop]):
#         params = upload_options.get(upload, {})
#         pinterest.upload_pin(
#             board_id=board_id,
#             image_file=x['Image Address'],
#             description=params["description"](x),
#             title=params["title"](x),
#             section_id=None,
#             link=params["link"](x)
#         )
#         sleep(randint(40, 60))
        

def save_local():
    ask = input('Save to local directory(y/n)? ').lower()
    if ask == 'y':
        # Dapatkan path dari folder program (tempat script Python dijalankan)
        program_dir = os.path.dirname(os.path.abspath(__file__))

        # Tampilkan daftar subfolder dalam folder program
        subfolders = [f for f in os.listdir(program_dir) if os.path.isdir(os.path.join(program_dir, f))]
        print("Pilih subfolder untuk menyimpan file:")
        for i, folder in enumerate(subfolders, start=1):
            print(f"{i}. {folder}")
        print(f"{len(subfolders) + 1}. Buat subfolder baru")

        # Pilih opsi
        choice = int(input("Masukkan nomor pilihan: "))

        if choice == len(subfolders) + 1:
            # Jika opsi terakhir dipilih, buat subfolder baru
            new_folder_name = input("Masukkan nama subfolder baru: ")
            subfolder_path = os.path.join(program_dir, new_folder_name)
            os.makedirs(subfolder_path, exist_ok=True)
        else:
            # Pilih subfolder dari daftar yang ada
            subfolder_path = os.path.join(program_dir, subfolders[choice - 1])

        # Nama dan isi file yang akan disimpan
        filename = "contoh.txt"
        file_content = "Ini adalah contoh isi file."

        # Path lengkap untuk file di dalam subfolder
        file_path = os.path.join(subfolder_path, filename)

        # Simpan file di dalam subfolder
        with open(file_path, "w") as file:
            file.write(file_content)

        print(f"File berhasil disimpan di {file_path}")
    else:
        pass

def load_local():
    # Dapatkan path dari folder program (tempat script Python dijalankan)
    program_dir = os.path.dirname(os.path.abspath(__file__))

    # Tampilkan daftar subfolder dalam folder program
    subfolders = [f for f in os.listdir(program_dir) if os.path.isdir(os.path.join(program_dir, f))]
    if not subfolders:
        print("Tidak ada subfolder yang tersedia.")
    else:
        print("Pilih subfolder:")
        for i, folder in enumerate(subfolders, start=1):
            print(f"{i}. {folder}")

        # Pilih subfolder dari daftar yang ada
        choice = int(input("Masukkan nomor pilihan: "))
        subfolder_path = os.path.join(program_dir, subfolders[choice - 1])

        # Tampilkan daftar file dalam subfolder yang dipilih
        files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
        if files:
            print("\nPilih file untuk dibuka:")
            for i, file_name in enumerate(files, start=1):
                print(f"{i}. {file_name}")
            
            file_choice = int(input("Masukkan nomor file pilihan: "))

            # Path lengkap untuk file yang dipilih
            selected_file_path = os.path.join(subfolder_path, files[file_choice - 1])

            # Buka dan tampilkan isi file yang dipilih
            with open(selected_file_path, "r") as file:
                print("\nIsi file:")
                print(file.read())
        else:
            print("Tidak ada file di dalam subfolder ini.")


# def display_data_tkinter(data):
#     root = tk.Tk()
#     root.title("Pinterest Pin Data")
#     root.geometry("800x600")  # Atur lebar window menjadi 800px dan tinggi 600px

#     # Frame utama untuk menambahkan scrollbar
#     frame = tk.Frame(root)
#     frame.pack(fill=tk.BOTH, expand=True)

#     # Buat scrollbar vertikal dan horizontal
#     tree_x_scroll = tk.Scrollbar(frame, orient="horizontal")
#     tree_y_scroll = tk.Scrollbar(frame, orient="vertical")

#     # Buat tabel menggunakan Treeview
#     columns = list(data[0].keys())
#     tree = ttk.Treeview(
#         frame, columns=columns, show='headings', 
#         xscrollcommand=tree_x_scroll.set, 
#         yscrollcommand=tree_y_scroll.set
#     )
    
#     tree_x_scroll.config(command=tree.xview)
#     tree_y_scroll.config(command=tree.yview)
#     tree_x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
#     tree_y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

#     for col in columns:
#         tree.heading(col, text=col, command=lambda _col=col: sort_column(tree, _col, False))
#         tree.column(col, anchor='center', width=100)  # Atur lebar kolom agar pas di window 800px
    
#     for item in data:
#         tree.insert('', 'end', values=[item[col] for col in columns])
    
#     tree.pack(fill=tk.BOTH, expand=True)

#     # Tombol Save
#     save_button = tk.Button(root, text="Save", command=lambda: save_excel(data))
#     save_button.pack(side=tk.LEFT, padx=10, pady=5)

#     # Tombol Close
#     close_button = tk.Button(root, text="Close", command=root.destroy)
#     close_button.pack(side=tk.RIGHT, padx=10, pady=5)

#     root.mainloop()

# def sort_column(tree, col, reverse):
#     l = [(tree.set(k, col), k) for k in tree.get_children('')]
#     l.sort(reverse=reverse)

#     # Reorder items in sorted positions
#     for index, (val, k) in enumerate(l):
#         tree.move(k, '', index)

#     # Toggle sort order for next click
#     tree.heading(col, command=lambda _col=col: sort_column(tree, _col, not reverse))

def main():
    while True:
        # pinterest = 
        if pinterest:
            while True:
                pin_search = pinterest.search(scope='pins', query='poster print')
                hasil = pin_search[0:10]
                pins = process_and_sort_pins(pinterest=pinterest, data=hasil)
                pilihan = input("Apakah Anda ingin menggunakan akun lain? (y/n): ").strip().lower()
                if pilihan == 'y':
                    break  # kembali untuk memilih akun baru
                elif pilihan == 'n':
                    print("Selesai. Keluar dari program.")
                    return  # keluar dari program
                else:
                    print("Input tidak valid, pilih 'y' atau 'n'.")

main()