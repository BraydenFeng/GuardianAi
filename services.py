def process_user_data(db, cipher, dataloader, uid: str):
    user = db.collection("users").document(uid).get()
    user_info = user.to_dict()

    discord_user = user_info["discord_username"]
    discord_token = user_info["discord_token"]

    decrypted_token = cipher.decrypt(discord_token)
    data = dataloader.results(decrypted_token, discord_user)

    return data


