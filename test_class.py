class download_picture:
    def __init__(self, step ,stage, dateStart):
        self.step = step
        self.stage = stage
        self.dateStart = dateStart

    def call_step(self):
        print(self.step)
    
    def call_stage(self):
        print(self.stage)

    def call_js(self):
        js = f"""{self.dateStart}"""
        print("js 輸出:", js)

if __name__ == "__main__":
    class_handles = [
        download_picture("330", "100", "20200325"), 
        download_picture("11", "300", "20200326")
    ]
    # de_handles = [obj.call_step() for obj in class_handles]
    for i in range(len(class_handles)):
        download = class_handles[i]
        download.call_step()
        download.call_stage()
        download.call_js()

# 330
# 100
# js 輸出: 20200325
# 11
# 300
# js 輸出: 20200326