import pygame
import time

def calculate_bpm(spacebar_press_times):
    if len(spacebar_press_times) < 2:
        return 0

    # Calculate time differences between consecutive spacebar presses
    time_diffs = [spacebar_press_times[i] - spacebar_press_times[i - 1] for i in range(1, len(spacebar_press_times))]

    # Convert time differences to beats per minute
    total_time = sum(time_diffs)
    avg_time_diff = total_time / len(time_diffs)
    bpm = 60 / avg_time_diff

    return bpm

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 200))  # Set screen size
    pygame.display.set_caption("BPM Calculator")  # Set window title

    font = pygame.font.Font(None, 36)

    spacebar_press_times = []
    running = True
    text_visible = True
    flash_duration = 0.05  # Duration to briefly flash the text (in seconds)

    print("Press the spacebar to measure BPM. After 5 seconds the BPM will be calculated.")

    # Display initial text
    text = font.render("Tap Spacebar", True, (255, 255, 255))
    text_rect = text.get_rect(center=(200, 100))
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Wait for spacebar press to start the timer
    spacebar_pressed = False

    while not spacebar_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                spacebar_pressed = True
                start_time = time.time()
            elif event.type == pygame.QUIT:
                running = False
                break

    while running and time.time() - start_time < 5:
        screen.fill((0, 0, 0))  # Fill the screen with black background

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                spacebar_press_times.append(time.time())
                text_visible = False  # Hide the text
                flash_start_time = time.time()  # Record the time when the flash starts

            elif event.type == pygame.QUIT:
                running = False
                break  # Exit loop if the window is closed

        if not text_visible and time.time() - flash_start_time < flash_duration:
            # Display "Click Here" text during the flash duration
            screen.blit(text, text_rect)
        else:
            text_visible = True  # Revert back to showing the text

        pygame.display.flip()  # Update the display

    pygame.quit()

    bpm = calculate_bpm(spacebar_press_times)
    print(f"BPM: {bpm}")
