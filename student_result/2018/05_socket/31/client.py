import socket
import threading
import os.path as op
from os import makedirs, listdir, system

SERVER_IP = '127.0.0.1'
SERVER_PORT = 50000
ADDRESS = (SERVER_IP, SERVER_PORT)

ABSPATH = op.dirname(op.abspath(__file__)) + '\\downloaded\\'

makedirs(ABSPATH, exist_ok=True)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.connect(ADDRESS)

print('=======PYSHARE=======')
print('서버에 연결되었습니다.')
print('도움말을 보시려면 \'help\'를 입력하세요.')


def showhelp():
    print('upload [name]: 파일을 저장소에 업로드 합니다. 그 이름은 name으로 저장됩니다.')
    print('download [name]: 이름이 name인 파일을 저장소에서 다운로드 합니다.')
    print('list: 저장소에 현재 있는 파일들의 목록을 보여줍니다.')
    print('myfiles: 현재 내가 다운로드한 파일들의 목록을 보여줍니다.')
    print('help: 명령어 리스트를 보여줍니다.')
    print('quit: 프로그램을 종료합니다.')


def uploadfile():
    try:
        uploadname = input('파일 경로를 입력해주세요: ')
        f = open(uploadname, 'rb')
        server_sock.send(b'ok')
        upload = f.read(4096)
        while upload:
            server_sock.send(upload)
            upload = f.read(4096)
        server_sock.send(b'fileend')
        print('{}가 성공적으로 업로드 되었습니다!'.format(uploadname.split('\\')[-1]))
        f.close()

    except FileNotFoundError:
        print('해당 파일은 존재하지 않습니다!')
        server_sock.send(b'error')


def downloadfile(name):
    isOk = server_sock.recv(4096).decode('UTF-8')
    if isOk == 'error':
        print('해당 파일은 존재하지 않습니다!')
    else:
        downloadname = input('다운로드 될 파일의 이름을 입력하세요(공백으로 놔두면 이름이 바뀌지 않습니다)\n> ')
        if downloadname == '':
            downloadname = name

        f = open(ABSPATH + downloadname, 'wb')
        download = server_sock.recv(1024)
        while True:
            if b'fileend' in download:
                download.replace(b'fileend', b'')
                f.write(download)
                break
            f.write(download)
            download = server_sock.recv(1024)

        print('{}가 다운로드 되었습니다.'.format(args[1]))
        f.close()


def listname():
    data = server_sock.recv(8192).decode('UTF-8').split()
    for names in data:
        print(names)


def showmyfiles():
    lists = listdir(ABSPATH)
    for names in lists:
        print(names)


while True:
    get = input('>>')

    if not get:
        continue

    args = get.split()
    server_sock.send(bytes(get, 'UTF-8'))

    try:
        if args[0] == 'quit':
            break

        elif args[0] == 'help':
            showhelp()

        elif args[0] == 'list':
            listname()

        elif args[0] == 'upload':
            uploadfile()

        elif args[0] == 'download':
            downloadfile(args[1])

        elif args[0] == 'myfiles':
            showmyfiles()

        else:
            print('명령어가 존재하지 않습니다.')

    except IndexError:
        print('명령어 형식이 잘못되었습니다.')


print('프로그램이 종료되었습니다.')
