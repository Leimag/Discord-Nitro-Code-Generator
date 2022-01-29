import threading, string, random, ctypes, os, time

total = 0

codesint = int(input("How many codes to generate: "))

print('Generating code\'s in the background..')

s = time.time()

def nitro():
    global total, checked
    while True:
        if total == codesint:
            break
        c = ''
        
        
        c += string.ascii_uppercase
        c += string.ascii_lowercase
        c += string.digits
        
        cd = ''.join(random.choice(c) for i in range(16))
        total += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Code Generator | Generated: {total}")

        with open('nitro_dump.txt', 'a') as f:
            f.write(cd + '\n')
    
    os.system('cls')
    print(f'Generated {total} codes, check nitro_dump.txt to view codes.')
    x = time.time()
    print(f'Took {round(x-s,2)} seconds to complete.')
    input('')
    exit()

        
        
            

            
            
            
    
    
    
    





    
    
thread = []
for i in range(5000):
    if total == codesint:
        break
    t = threading.Thread(target=nitro)
    t.start()
    thread.append(t)
    for x in thread:
        x.join()

        


