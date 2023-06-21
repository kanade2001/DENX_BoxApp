import lcd

def main(line1, line2):
    l = lcd.HD44780()
    l.string(line1, 1)
    l.strint(line2, 2)
    
if __name__ == "__main__":
    main("LCD Monitor", "sample123")