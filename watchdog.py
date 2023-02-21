import os, shutil, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "C:/Users/adils/Downloads"
dest = "C:/Users/adils/Desktop"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(event):
        name,ext = os.path.splitext(event.source);
        for key,value in dir_tree.items():
            if ext in value:
                fileName = os.path.basename(event.source);
                path1 = source + "/" + fileName
                path2 = dest + "/" + key
                path3 = dest + "/" + key + "/" + fileName
                time.sleep(3)
                if os.path.exists(path2):
                    print("Moving " + fileName)
                    shutil.move(path1, path3);
                else:
                    os.makedirs(path2);
                    print("Moving " + fileName)
                    shutil.move(path1, path3);


Event_Handler = FileMovementHandler()
observer = Observer();
observer.schedule(Event_Handler, source, recursive = True)
observer.start();
try:
    while True:
        time.sleep(2);
        print("The watchdog is watching.");
except KeyboardInterrupt:
    print("Observer Stopped");
    observer.stop();

    
