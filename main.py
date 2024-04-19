import pygame
import os
import time

# Initialisiere Pygame
pygame.init()

# Einstellungen für den Vollbildmodus
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Chürz und Quer Challange")

# Verzeichnis mit den Bildern
image_dir = "resources/images"


# Liste der Bilder im Verzeichnis
image_files = os.listdir(image_dir)
image_files = [file for file in image_files if file.endswith(('.bmp'))]

# Lade die Bilder
images = []
for img in image_files:
    image = pygame.image.load(os.path.join(image_dir, img)).convert()
    images.append(image)

# Index des aktuellen Bildes
current_image = 0


# Zähler für die Anzahl der Leertastendrücke
space_press_count = 0

# Zeitpunkt des letzten Tastendrucks
last_keypress_time = time.time()

# Hauptprogrammschleife
running = True
while running:
    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                space_press_count += 1
                if space_press_count >= 10:
                    # Wenn 10 Mal die Leertaste gedrückt wurde, zeige das nächste Bild an
                    current_image = min(current_image + 1, len(images) - 1)
                    last_keypress_time = time.time()
                    space_press_count = 0  # Zähler zurücksetzen

    # Überprüfe, ob 30 Sekunden vergangen sind
    if time.time() - last_keypress_time > 5:
        # Zurück zum ersten Bild
        current_image = 0

    # Hintergrund löschen und Bild anzeigen
    screen.fill((0, 0, 0))
    image = images[current_image]

    # Skaliere das Bild auf die Bildschirmgröße
    image = pygame.transform.scale(image, screen.get_size())

    # Bildschirm aktualisieren
    screen.blit(image, (0, 0))
    pygame.display.flip()

# Pygame beenden
pygame.quit()
