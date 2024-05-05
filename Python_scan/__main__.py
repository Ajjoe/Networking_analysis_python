from Pythan_scan import run as run_scan
from sniffer import run as run_sniffer
from datetime import datetime
print("please enter the choice of tools you would like to use\n")
print("input 'Scan' to scan a target for open ports and 'sniff' to Sniff and get the ethernet frame of incoming packets\n")
print("Please be aware these are tools and NOT mean't to illegally gain or steal information from organizations or individuals")
choice = input("Please input your choice ")
def choice_tool():
    if choice == 'Scan':
        target = input('Please input the target ')
        end_port = int(input('Please input the end_port '))
        start_port = int(input('Please input the start_port '))
        print("-" * 50)
        print(f"Scanning {target} started at {datetime.now()}")
        print("-" * 50)
        run_scan(start_port , end_port, target) 
    elif choice == 'Sniff':
        run_sniffer()
    else: print("this was not a valid input")
def main():
    choice_tool()

if __name__ == '__main__':
    main()
