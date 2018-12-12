from multiprocessing import Process
import time

class Schedule():
    @staticmethod
    def check_proxy():
        i = 0;
        while i < 3:
            print('geting')
            time.sleep(2)
            i+=1

    @staticmethod
    def valid_proxy():
        pass

    def run(self):
        check_process = Process(target = Schedule.check_proxy)
        check_process.start()

def main():
    sss = Schedule()
    sss.run()

if __name__ == '__main__':
    main()