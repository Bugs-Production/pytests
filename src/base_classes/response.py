from src.enums.global_enums import GlobalErrorMessages


class Response:
    """Класс для проверки валидации и статус ответов"""

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate(self, schema: object) -> None:  # валидация данных
        if "data" in self.response_json:  # Проверяем наличие ключа "data"
            data = self.response_json["data"]
            if isinstance(data, list):
                for item in data:
                    schema.model_validate(item)
            else:
                schema.model_validate(data)
        else:
            schema.model_validate(self.response_json)

    def validate_count(self, count: int) -> None:  # проверка кол-ва элементов
        count_elements = len(self.response_json)
        assert len(self.response_json) == count, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value.format(count,
                                                                                                      count_elements)

    def assert_status_code(self, status_code: int) -> None:  # проверка на статус код
        assert self.response_status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value.format(status_code,
                                                                                                            self.response_status_code)
