import os
import sys
from random import choice
from SpamX import (OWNER_ID, HNDLR, SUDO_USERS, hl)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *

REPLY = ( "AJA", "TERI", "MAA", "KI", "CHUT", "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP", "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA", " ADITYA", "AAGYA", "TERI", "MAA ", "CHODNE", "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE", "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI", "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE", "BOOBS", "DABAUNGA","XXX","TERI","MAA","KAA","CHUT","MARU","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA","MARU","SUAR","KEE","CHODE","TERI","MAAA","KEEE","NUDES","BECHUNGA","RANDI","KEE","PILLE","TERI","MAAA","CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUKAT","BANAA","LODE","TERAA","BAAP","HUU","TERI","GFF","KAA","BHOSDAA","MARUU","MADHARCHOD","TERI ","NANAI","KAA","CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR","GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR","KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE","MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE","JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI","MAA","KAAA","BOOBS","DABAA","KEE","PHODD","DUNGAA","SUARRR","AUKATT","BANAA","BEHEN","KEEE","LODEE","FARAARR","MAAT","HONAA","KIDD","APNNII","MAAA","KII","CHUDAII","DEKHH","KEEE","CHUTT","LEJAA","TERI","GFF","KOO","BHEJ","DENAA","KIDDDX","URR","DADD","HEREE","BAAP","BOLL","KEEE","JANAA","LODEE", )

@Client.on_message(filters.command(["abuse", "gali"], ".") & filters.me)
async def abuse(client: Client, msg: Message): 
        await msg.edit(random.choice(RAID))



add_command_help("Abuse",)
    
        [".abuse", "To Abuse Someone."],
    

