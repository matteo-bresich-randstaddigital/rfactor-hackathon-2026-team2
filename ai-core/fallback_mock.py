def get_fallback_response():
    # Rete di sicurezza (No Playback ok, ma evita il blocco totale della UI)
    return {
        "score": 85,
        "recommended_action": "Delegate",
        "reasoning": "Fallback mode attivo: delega suggerita in assenza di rete.",
        "draft_message": "Gentile collega, delego il meeting a [Nome Junior]."
    }
