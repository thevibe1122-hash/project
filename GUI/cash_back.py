import sys,os
def cash_back(q,betted):
    
    if q == "🍉":
        return 2*betted
    elif q == "🍋":
        return 3*betted
    elif q == "🔔":
        return 4*betted

def get_data_file_path(filename):
    if getattr(sys, 'frozen', False):
        # Running as bundled exe
        base_dir = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'SlotMachineV')
        os.makedirs(base_dir, exist_ok=True)
        return os.path.join(base_dir, filename)
    else:
        # Running as script
        return filename

# Then replace every occurrence of "highscore.json" with:
file_path = get_data_file_path("highscore.json")
    

  
