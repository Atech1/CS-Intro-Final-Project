# Alexander Ross (asr3bj) and Tilden (tw8rt), UI.py
# this was created Nov, 2017
import gamebox

Draw_Layers = dict()
Draw_Objects = []
UI_Elements = []
Controls = []


class Camera(gamebox.Camera):
    def __init__(self, width, height, full_screen = False, children = None):
        gamebox.Camera.__init__(self, width, height, False)
        self.view = gamebox.from_color(width / 2, height / 2, "white", width, height)
        self.children = children

    def move(self, x, y = None):
        if y is None: x, y = x
        self.x += x
        self.y += y
        self.view.move(x, y)
        if self.children is not None: self.children.move(x, y)

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)


class TextObject:
    def create_boxes(self, text, x, y, color, textDes):
        all_boxes = []
        print(text.split("\n"))
        for i in range(len(text.split("\n")) - 1):
            line = text.split("\n")[i]
            print(line, i)
            all_boxes.append(gamebox.from_text(x, y + 20 * i, line,
                                               textDes['font'], textDes['size'], color))
        return all_boxes

    def __init__(self, text, x, y, color = "black", textDes = None, image = None):
        self.boxes = list()
        self.text = text
        self.width = x
        self.height = y
        self.textDes = textDes

    def contains(self, x, y):
        for box in self.boxes:
            if box.contains(x, y):
                return True
            else:
                return False

    def move(self, x, y):
        for box in self.boxes:
            box.move(x, y)
        return

    def add_to_draw(self):
        for box in self.boxes:
            Draw_Objects.append(box)


class Button(TextObject):
    def __init__(self, x, y, text, color = "black", textDes = None, image = None):  # auto generated
        TextObject.__init__(self, text, x, y, color, textDes)
        self.boxes = self.create_boxes(self.text, self.width, self.height, color, textDes)
        UI_Elements.append(self)
        self.add_to_draw()

    def On_Click(self):
        print("click")
        return

    def Hover(self):

        return

    def Mouse_Check(self, x, y):
        if self.contains(x, y):
            self.Hover()
        return




def TextDescriptor(font = 'arial', text = "", size = 20, bold = False, italic = False):  # auto generated
    instance_TextDescriptor = dict()
    instance_TextDescriptor['font'] = font
    instance_TextDescriptor['text'] = text
    instance_TextDescriptor['size'] = size
    instance_TextDescriptor['bold'] = bold
    instance_TextDescriptor['italic'] = italic
    return instance_TextDescriptor


def drawing(camera):
    for item in Draw_Objects:
        camera.draw(item)
    camera.display()
    return


def check_controls(keys):
    for control in Controls:
        if control: return
    return


def check_mouse(camera):
    x, y = camera.mouse
    for element in UI_Elements:
        if getattr(element, "Mouse_Check", False):
            element.Mouse_Check(x, y)
            if camera.mouseclick:
                element.On_Click()
    return
