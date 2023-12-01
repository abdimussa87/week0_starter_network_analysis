from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
class DBWithSchema:
    def __init__(self) -> None:
        self.client = MongoClient(os.environ["DB_URL"])
        self.db = self.client["slack_database"]

        self.channels_validator = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ['id',"name", "created", "creator",'is_archived','is_general','members','topic','purpose'],
                "properties": {
                    "id": {"bsonType": "string"},
                    "name": {"bsonType": "string"},
                    "created": {"bsonType": "int"},
                    "creator": {"bsonType": "string"},
                    "is_archived": {"bsonType": "bool"},
                    "is_general": {"bsonType": "bool"},
                    "members": {
                        "bsonType": "array",
                        "items": {"bsonType": "string"}
                    },
                    "topic": {
                        "bsonType": "object",
                        "properties": {
                            "value": {"bsonType": "string"},
                            "creator": {"bsonType": "string"},
                            "last_set": {"bsonType": "int"}
                        }
                    },
                    "purpose": {
                        "bsonType": "object",
                        "properties": {
                            "value": {"bsonType": "string"},
                            "creator": {"bsonType": "string"},
                            "last_set": {"bsonType": "int"}
                        }
                    }
            }
            }
        }
        self.users_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["id", "team_id", "name", "deleted", "color", "real_name", "tz", "tz_label", "tz_offset", "profile", "is_admin", "is_owner", "is_primary_owner", "is_restricted", "is_ultra_restricted", "is_bot", "is_app_user", "updated", "is_email_confirmed", "who_can_share_contact_card"],
            "properties": {
                "id": {"bsonType": "string"},
                "team_id": {"bsonType": "string"},
                "name": {"bsonType": "string"},
                "deleted": {"bsonType": "bool"},
                "color": {"bsonType": "string"},
                "real_name": {"bsonType": "string"},
                "tz": {"bsonType": "string"},
                "tz_label": {"bsonType": "string"},
                "tz_offset": {"bsonType": "int"},
                "profile": {
                    "bsonType": "object",
                    "required": ["title", "phone", "skype", "real_name", "real_name_normalized", "display_name", "display_name_normalized", "fields", "status_text", "status_emoji", "status_emoji_display_info", "status_expiration", "avatar_hash", "image_original", "is_custom_image", "email", "huddle_state", "first_name", "last_name", "image_24", "image_32", "image_48", "image_72", "image_192", "image_512", "image_1024", "status_text_canonical", "team"],
                    "properties": {
                        "title": {"bsonType": "string"},
                        "phone": {"bsonType": "string"},
                        "skype": {"bsonType": "string"},
                        "real_name": {"bsonType": "string"},
                        "real_name_normalized": {"bsonType": "string"},
                        "display_name": {"bsonType": "string"},
                        "display_name_normalized": {"bsonType": "string"},
                        "fields": {"bsonType": "object"},
                        "status_text": {"bsonType": "string"},
                        "status_emoji": {"bsonType": "string"},
                        "status_emoji_display_info": {"bsonType": "array"},
                        "status_expiration": {"bsonType": "int"},
                        "avatar_hash": {"bsonType": "string"},
                        "image_original": {"bsonType": "string"},
                        "is_custom_image": {"bsonType": "bool"},
                        "email": {"bsonType": "string"},
                        "huddle_state": {"bsonType": "string"},
                        "first_name": {"bsonType": "string"},
                        "last_name": {"bsonType": "string"},
                        "image_24": {"bsonType": "string"},
                        "image_32": {"bsonType": "string"},
                        "image_48": {"bsonType": "string"},
                        "image_72": {"bsonType": "string"},
                        "image_192": {"bsonType": "string"},
                        "image_512": {"bsonType": "string"},
                        "image_1024": {"bsonType": "string"},
                        "status_text_canonical": {"bsonType": "string"},
                        "team": {"bsonType": "string"}
                    }
                },
                "is_admin": {"bsonType": "bool"},
                "is_owner": {"bsonType": "bool"},
                "is_primary_owner": {"bsonType": "bool"},
                "is_restricted": {"bsonType": "bool"},
                "is_ultra_restricted": {"bsonType": "bool"},
                "is_bot": {"bsonType": "bool"},
                "is_app_user": {"bsonType": "bool"},
                "updated": {"bsonType": "int"},
                "is_email_confirmed": {"bsonType": "bool"},
                "who_can_share_contact_card": {"bsonType": "string"}
            }
        }

    }
        self.channel_message_validator = {
            "$jsonSchema": {
            "bsonType": "object",
            "properties": {
                "name": {"bsonType": "string"},
                "client_msg_id": {"bsonType": "string"},
                "type": {"bsonType": "string"},
                "text": {"bsonType": "string"},
                "user": {"bsonType": "string"},
                "ts": {"bsonType": "string"},
                "blocks": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "object",
                        "properties": {
                            "type": {"bsonType": "string"},
                            "block_id": {"bsonType": "string"},
                            "elements": {
                                "bsonType": "array",
                                "items": {
                                    "bsonType": "object",
                                    "properties": {
                                        "type": {"bsonType": "string"},
                                        "elements": {
                                            "bsonType": "array",
                                            "items": {
                                                "bsonType": "object",
                                                "properties": {
                                                    "type": {"bsonType": "string"},
                                                    "url": {"bsonType": "string"},
                                                    "text": {"bsonType": "string"}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "team": {"bsonType": "string"},
                "user_team": {"bsonType": "string"},
                "source_team": {"bsonType": "string"},
                "user_profile": {
                    "bsonType": "object",
                    "properties": {
                        "avatar_hash": {"bsonType": "string"},
                        "image_72": {"bsonType": "string"},
                        "first_name": {"bsonType": "string"},
                        "real_name": {"bsonType": "string"},
                        "display_name": {"bsonType": "string"},
                        "team": {"bsonType": "string"},
                        "name": {"bsonType": "string"},
                        "is_restricted": {"bsonType": "bool"},
                        "is_ultra_restricted": {"bsonType": "bool"}
                    }
                },
                "attachments": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "object",
                        "properties": {
                            "from_url": {"bsonType": "string"},
                            "ts": {"bsonType": "int"},
                            "image_url": {"bsonType": "string"},
                            "image_width": {"bsonType": "int"},
                            "image_height": {"bsonType": "int"},
                            "image_bytes": {"bsonType": "int"},
                            "service_icon": {"bsonType": "string"},
                            "id": {"bsonType": "int"},
                            "original_url": {"bsonType": "string"},
                            "fallback": {"bsonType": "string"},
                            "text": {"bsonType": "string"},
                            "title": {"bsonType": "string"},
                            "title_link": {"bsonType": "string"},
                            "service_name": {"bsonType": "string"},
                            "fields": {
                                "bsonType": "array",
                                "items": {
                                    "bsonType": "object",
                                    "properties": {
                                        "value": {"bsonType": "string"},
                                        "title": {"bsonType": "string"},
                                        "short": {"bsonType": "bool"}
                                    }
                                }
                            }
                        }
                    }
                }
            }
            }
        }
        try:
            self.db.create_collection("channels")
            self.db.create_collection("users")
            self.db.create_collection("channel_messages")
            self.db.create_collection("channel_messages_test")
            self.db.create_collection("channel_messages_reactions")
        except Exception as e:
            print(e)

        self.db.command("collMod", "users", validator=self.users_validator)
        self.db.command("collMod", "channels", validator=self.channels_validator)
        self.db.command("collMod", "channel_messages", validator=self.channel_message_validator)

    def list_collections(self):
        return self.db.list_collection_names()
    
    def get_validation(self, collection_name: str):
        self.check_if_collection_exist(collection_name)
        return self.db.get_collection(collection_name).options()
    
    def check_if_collection_exist(self, collection_name: str):
        if not self.list_collections().__contains__(collection_name):
            self.db.create_collection(collection_name)
            
    def insert_to_collection(self, collection_name, data):
        self.check_if_collection_exist(collection_name)
        collection = self.db[collection_name]
        return collection.insert_one(data)

    def insert_many_to_collection(self, collection_name, data):
        self.check_if_collection_exist(collection_name)
        result = self.db[collection_name].insert_many(data)
        return result.inserted_ids

    def find_all(self, collection_name):
        self.check_if_collection_exist(collection_name)
        return self.db[collection_name].find()

    def find(self, collection_name, key, value):
        self.check_if_collection_exist(collection_name)
        return self.db[collection_name].find({key: value})
    
    def find_by_id(self, collection_name, _id):
        self.check_if_collection_exist(collection_name)
        return self.db[collection_name].find

    def find_one(self, collection_name, key, value):
        self.check_if_collection_exist(collection_name)
        return self.db[collection_name].find_one({key: value})