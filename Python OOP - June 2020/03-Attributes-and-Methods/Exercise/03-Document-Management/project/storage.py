class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [i for i in self.categories if i.id == category_id]
        if not category: return

        category = category[0]
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [i for i in self.topics if i.id == topic_id]
        if not topic: return

        topic = topic[0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = [i for i in self.documents if i.id == document_id]
        if not document: return

        document = document[0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [i for i in self.categories if i.id == category_id]
        if not category: return

        category = category[0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [i for i in self.topics if i.id == topic_id]
        if not topic: return

        topic = topic[0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [i for i in self.documents if i.id == document_id]
        if not document: return

        document = document[0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = [i for i in self.documents if i.id == document_id]
        if not document: return

        document = document[0]

        return document

    def __repr__(self):
        return "\n".join(f'{document}' for document in self.documents)