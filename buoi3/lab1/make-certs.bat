@echo off
setlocal enabledelayedexpansion
cd /d %~dp0

:: Tim duong dan openssl
where openssl >nul 2>nul
if %errorlevel% equ 0 (
    set "OPENSSL=openssl"
) else if exist "C:\Program Files\Git\usr\bin\openssl.exe" (
    set "OPENSSL=C:\Program Files\Git\usr\bin\openssl.exe"
) else if exist "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" (
    set "OPENSSL=C:\Program Files\OpenSSL-Win64\bin\openssl.exe"
) else (
    echo [!] Khong tim thay OpenSSL. Vui long cai dat hoac them OpenSSL vao PATH.
    pause
    exit /b 1
)

mkdir certs\ca 2>nul
mkdir certs\server 2>nul
mkdir certs\client 2>nul

echo Generating CA...
"%OPENSSL%" genrsa -out certs\ca\ca.key 2048
"%OPENSSL%" req -x509 -new -nodes -key certs\ca\ca.key -sha256 -days 3650 -out certs\ca\ca.crt -config openssl.cnf -extensions v3_ca

echo Generating Server Certificate...
"%OPENSSL%" genrsa -out certs\server\server.key 2048
"%OPENSSL%" req -new -key certs\server\server.key -out certs\server\server.csr -subj "/C=VN/ST=HN/L=HN/O=MyOrg/OU=IT Dept/CN=localhost"
"%OPENSSL%" x509 -req -in certs\server\server.csr -CA certs\ca\ca.crt -CAkey certs\ca\ca.key -CAcreateserial -out certs\server\server.crt -days 365 -sha256

echo Generating Client Certificate...
"%OPENSSL%" genrsa -out certs\client\client.key 2048
"%OPENSSL%" req -new -key certs\client\client.key -out certs\client\client.csr -subj "/C=VN/ST=HN/L=HN/O=MyOrg/OU=IT Dept/CN=client"
"%OPENSSL%" x509 -req -in certs\client\client.csr -CA certs\ca\ca.crt -CAkey certs\ca\ca.key -CAcreateserial -out certs\client\client.crt -days 365 -sha256

move certs\ca\ca.srl certs\ca\ca.srl.bak >nul 2>&1
echo.
echo ===============================
echo Cac chung chi da tao xong!
echo - CA: certs\ca\
echo - Server: certs\server\
echo - Client: certs\client\
echo ===============================
