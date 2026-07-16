import urllib.request
import json
import os

def update_fortnite():
    print("[*] Récupération des offsets Fortnite...")
    # URL d'un dumper communautaire fiable et mis à jour automatiquement
    url = "https://raw.githubusercontent.com/paysonism/Fortnite-Offsets/main/offsets.json"
    
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        
        # Format attendu par notre DLL
        fortnite_json = {
            "GWorld": int(data.get("GWorld", 0)),
            "GNames": int(data.get("GNames", 0)),
            "pattern_GWorld": "48 8B 1D ?? ?? ?? ?? 48 85 DB 74",
            "pattern_GNames": "48 8B 05 ?? ?? ?? ?? 48 85 C0 74 ?? 48 8B 40 ?? C3",
            "UWorld_GameState": int(data.get("UWorld", {}).get("GameState", 360)),
            "UWorld_OwningGameInstance": int(data.get("UWorld", {}).get("OwningGameInstance", 280)),
            "UGameInstance_LocalPlayers": int(data.get("UGameInstance", {}).get("LocalPlayers", 56)),
            "APlayerController_AcknowledgedPawn": int(data.get("APlayerController", {}).get("AcknowledgedPawn", 848)),
            "APlayerController_PlayerCameraManager": int(data.get("APlayerController", {}).get("PlayerCameraManager", 880)),
            "APawn_PlayerState": int(data.get("APawn", {}).get("PlayerState", 600)),
            "ACharacter_Mesh": int(data.get("ACharacter", {}).get("Mesh", 792)),
            "APlayerState_TeamIndex": int(data.get("APlayerState", {}).get("TeamIndex", 3336)),
            "APlayerState_PawnPrivate": int(data.get("APlayerState", {}).get("PawnPrivate", 760)),
            "AGameState_PlayerArray": int(data.get("AGameState", {}).get("PlayerArray", 680)),
            "AGameState_PlayerArray_Size": int(data.get("AGameState", {}).get("PlayerArray_Size", 688)),
            "USceneComponent_RelativeLocation": int(data.get("USceneComponent", {}).get("RelativeLocation", 304)),
            "USkinnedMeshComponent_BoneArray": int(data.get("USkinnedMeshComponent", {}).get("BoneArray", 1432)),
            "USkinnedMeshComponent_BoneCount": int(data.get("USkinnedMeshComponent", {}).get("BoneCount", 1440)),
            "UFortAbilitySystemComponent_CurrentHealth": int(data.get("UFortAbilitySystemComponent", {}).get("CurrentHealth", 1528)),
            "APlayerCameraManager_CameraLocation": int(data.get("APlayerCameraManager", {}).get("CameraLocation", 4600)),
            "APlayerCameraManager_CameraRotation": int(data.get("APlayerCameraManager", {}).get("CameraRotation", 4612)),
            "APlayerCameraManager_FOV": int(data.get("APlayerCameraManager", {}).get("FOV", 4628))
        }
        
        with open("fortnite_offsets.json", "w") as f:
            json.dump(fortnite_json, f, indent=4)
        print("[+] Fichier fortnite_offsets.json mis à jour avec succès.")
        
    except Exception as e:
        print(f"[-] Erreur lors de la mise à jour de Fortnite: {e}")

def update_dayz():
    print("[*] Récupération des offsets DayZ...")
    # Modèle d'offsets DayZ de base (les structures Enfusion ne changent pas d'offset à chaque patch,
    # seules les adresses dynamiques bougent, gérées par le Pattern Scanner de la DLL).
    dayz_json = {
        "_comment": "DayZ Enfusion Engine — Offsets + Patterns AOB",
        "_version": "1.26+",
        "_engine": "Enfusion (Bohemia Interactive)",
        "pattern_WorldGameObject": "4C 89 A7 ?? ?? ?? ?? 48 8B 8F ?? ?? ?? ??",
        "pattern_EntityList": "48 8B 0D ?? ?? ?? ?? 48 85 C9 74 ?? 48 8B 01",
        "pattern_Camera": "48 8B 0D ?? ?? ?? ?? 48 85 C9 74 ?? 4C 8B 41",
        "pattern_LocalPlayer": "48 8B 05 ?? ?? ?? ?? 48 85 C0 74 ?? 48 8B 40 ??",
        "WorldGameObject_rip_offset": 3,
        "WorldGameObject_rip_size": 7,
        "EntityList_rip_offset": 3,
        "EntityList_rip_size": 7,
        "Camera_rip_offset": 3,
        "Camera_rip_size": 7,
        "LocalPlayer_rip_offset": 3,
        "LocalPlayer_rip_size": 7,
        "Entity_Position": 320,
        "Entity_Health": 528,
        "Entity_Name": 88,
        "Entity_Next": 16,
        "Entity_IsPlayer": 264,
        "Camera_ViewMatrix": 208,
        "EntityList_Count": 8,
        "EntityList_Data": 16
    }
    
    with open("dayz_offsets.json", "w") as f:
        json.dump(dayz_json, f, indent=4)
    print("[+] Fichier dayz_offsets.json initialisé/mis à jour.")

if __name__ == "__main__":
    update_fortnite()
    update_dayz()
