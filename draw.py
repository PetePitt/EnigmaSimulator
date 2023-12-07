import pygame


def draw(enigma, path, screen, width, height, margins, gap, font):
    # coordinate calcs
    x = margins["left"]
    y = margins["top"]
    w = (width-margins["left"]-margins["right"]-5*gap)/6
    h = height - margins["top"] - margins["bottom"]

    # path coordinates
    q = [margins["top"] + (signal+1)*h/27 for signal in path]
    p = [width-margins["right"]-w/2]
    for i in [4, 3, 2, 1, 0]:
        p.append(margins["left"]+(i)*(gap+w)+w*3/4)
        p.append(margins["left"]+(i)*(gap+w)+w*1/4)
    p.append(margins["left"]+w*3/4)
    for i in [1, 2, 3, 4]:
        p.append(margins["left"]+(i)*(gap+w)+w*1/4)
        p.append(margins["left"]+(i)*(gap+w)+w*3/4)
    p.append(width-margins["right"]-w/2)

    # draw path
    if len(path) > 0:
        for i in range(1, 21):
            if i < 10:
                color = "#43aa8b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (p[i-1], q[i-1])
            end = (p[i], q[i])
            pygame.draw.line(screen, color, start, end, width=4)

    # draw enigma components
    for component in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap

    # add names
    names = ["Reflector", "Left", "Middle", "Right", "Plugboard", "Key/Lamp"]
    y = margins["top"]*0.8


    for i in range(6):
        x = margins["left"] + w/2 + i*(w+gap)
        title = font.render(names[i], True, "white")
        text_box = title.get_rect(center=(x,y))
        screen.blit(title, text_box)