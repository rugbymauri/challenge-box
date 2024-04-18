import pygame
import os

# Initialisiere Pygame
pygame.init()

# Einstellungen für den Vollbildmodus
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Bildanzeige")

# Verzeichnis mit den Bildern
image_dir = "/pfad/zum/verzeichnis/der/bilder"

# Liste der Bilder im Verzeichnis
image_files = os.listdir(image_dir)
image_files = [file for file in image_files if file.endswith(('.jpg', '.png', '.jpeg'))]

# Lade die Bilder
images = [pygame.image.load(os.path.join(image_dir, img)).convert() for img in image_files]

# Index des aktuellen Bildes
current_image = 0

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
            elif event.key == pygame.K_RIGHT:
                # Nächstes Bild anzeigen
                current_image = (current_image + 1) % len(images)
            elif event.key == pygame.K_LEFT:
                # Vorheriges Bild anzeigen
                current_image = (current_image - 1) % len(images)

    # Hintergrund löschen und Bild anzeigen
    screen.fill((0, 0, 0))
    screen.blit(images[current_image], (0, 0))

    # Bildschirm aktualisieren
    pygame.display.flip()

# Pygame beenden
pygame.quit()
