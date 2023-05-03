'''
Main file
'''

print('-- WELCOME TO THE JENKINS INSTALLATION GUIDE --')
print('This guide was developed for NTT Data Windows Computers')
print()
print('Lets get started: download JDK 17 and the MSI Jenkins installer')
print('Now, install Java first, and Jenkins second')
print()
print('Now, proceed to open PowerShell with admin rights, and run the following scripts')
print(r'keytool -importcert -alias zscalerca -keystore C:\Program Files\Java\jdk-17\lib\security\cacerts -file C:\Users\jlozamoo\Downloads\Zscaler Root CA.crt')
print('When asked for a password, use changeit, and indicate yes or sí depending on your language')
print()
print('Go to the jenkins directory and open the xml file, so that you change the arguments')
print('Insert the following options pointing to the certificate we just moved')
print(r'-Djavax.net.ssl.trustStore=C:\Program Files\Java\jdk-17\lib\security\cacerts -Djavax.net.ssl.trustStorePassword=changeit')
print()
print('Finally, restart Jenkins and enjoy everything')
print('From PowerShell, go to the Jenkins directory and run the following')
print(r'.\jenkins.exe restart')