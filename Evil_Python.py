import platform
import os
from datetime import datetime
import json

try:
    from PIL import ImageGrab
    import pyautogui
    SCREENSHOT_AVAILABLE = True
except ImportError:
    SCREENSHOT_AVAILABLE = False
    print("⚠️  Screenshot libraries niet gevonden. Installeer met: pip install pillow pyautogui")


def verzamel_os_informatie():
    try:
        os_info = {
            "systeem": platform.system(),
            "versie": platform.version(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "platform": platform.platform(),
            "node_naam": platform.node(),
            "architectuur": platform.architecture()[0]
        }
        
        tijdstempel = (
            datetime.now().strftime("%Y-%m-%d"),
            datetime.now().strftime("%H:%M:%S"),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        os_info["datum"] = tijdstempel[0]
        os_info["tijd"] = tijdstempel[1]
        os_info["volledige_tijdstempel"] = tijdstempel[2]
        
        print("✅ OS informatie verzameld!")
        return os_info
        
    except Exception as e:
        print(f"❌ Fout bij het verzamelen van OS info: {e}")
        return None


def maak_screenshot(bestandsnaam="screenshot.png"):
    if not SCREENSHOT_AVAILABLE:
        print("❌ Screenshot libraries niet beschikbaar")
        return (False, None)
    
    try:
        screenshot = ImageGrab.grab()
        
        output_dir = "evil_python_output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        volledig_pad = os.path.join(output_dir, bestandsnaam)
        
        screenshot.save(volledig_pad)
        print(f"✅ Screenshot opgeslagen: {volledig_pad}")
        
        return (True, volledig_pad)
        
    except Exception as e:
        print(f"❌ Fout bij het maken van screenshot: {e}")
        return (False, None)


def sla_data_op(os_info, screenshot_pad):
    try:
        output_dir = "evil_python_output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        data = {
            "os_informatie": os_info,
            "screenshot_locatie": screenshot_pad,
            "status": "Gegevens succesvol verzameld"
        }
        
        json_pad = os.path.join(output_dir, "systeem_info.json")
        with open(json_pad, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Data opgeslagen in: {json_pad}")
        return True
        
    except Exception as e:
        print(f"❌ Fout bij het opslaan van data: {e}")
        return False


def toon_verzamelde_data(os_info):
    print("\n" + "="*50)
    print("🔴 RED SIGMA - SYSTEEM INFORMATIE")
    print("="*50)
    
    if os_info:
        for key, value in os_info.items():
            print(f"{key.upper():<25}: {value}")
    
    print("="*50 + "\n")


def verstuur_data_email(os_info, screenshot_pad):
    print("\n📧 Email functionaliteit (nog niet geïmplementeerd)")
    print("   Tip: Gebruik 'smtplib' en 'email' modules voor email verzending")
    print("   Voorbeeld: https://docs.python.org/3/library/smtplib.html")


def main():
    print("\n" + "🔴"*25)
    print("RED SIGMA - Evil_Python.exe")
    print("Educatieve hacking opdracht")
    print("🔴"*25 + "\n")
    
    try:
        print("📊 Stap 1: OS informatie verzamelen...")
        os_info = verzamel_os_informatie()
        
        if os_info:
            toon_verzamelde_data(os_info)
        
        print("📸 Stap 2: Screenshot maken...")
        screenshot_result = maak_screenshot(f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        success, screenshot_pad = screenshot_result
        
        print("\n💾 Stap 3: Data opslaan...")
        if os_info:
            sla_data_op(os_info, screenshot_pad)
        
        print("\n✅ Alle taken voltooid!")
        print("\n📝 Volgende stap: Maak een .exe met:")
        print("   pyinstaller --onefile Evil_Python.py")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Programma afgebroken door gebruiker")
    except Exception as e:
        print(f"\n❌ Onverwachte fout: {e}")
    
    input("\n\nDruk op Enter om af te sluiten...")


if __name__ == "__main__":
    main()
