from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from waitress import serve
import os
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Настройка для статических файлов
ASSETS_DIR = Path("./assets")
ASSETS_DIR.mkdir(exist_ok=True)

# Эндпоинт для отдачи статических изображений
@app.route('/assets/<path:filename>')
def serve_asset(filename):
    """Отдает статические файлы из папки assets"""
    return send_from_directory(ASSETS_DIR, filename)

# Реальные новости из примера (с правильными путями к изображениям)
ALL_NEWS = [
    {
        "id": "5bc71782-73f6-46bb-b1ad-c1ab94ee45dd",
        "title": "Встречаемся в СДЭК",
        "cover": {
            "type": "gallery",
            "images": [
                {
                    "s": "/assets/newsCover_1775225203-s.png",
                    "m": "/assets/newsCover_1775225203-m.png",
                    "l": "/assets/newsCover_1775225203-l.png",
                    "hd": "/assets/newsCover_1775225203-hd.png"
                },
                {
                    "s": "/assets/newsCover_1775225117-s.png",
                    "m": "/assets/newsCover_1775225117-m.png",
                    "l": "/assets/newsCover_1775225117-l.png",
                    "hd": "/assets/newsCover_1775225117-hd.png"
                }
            ]
        },
        "likeCount": 1,
        "viewCount": 28,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-04-03T13:59:05Z",
        "rubrics": [
            {"id": 10, "slug": "top", "name": "Важное для работы"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    },
    {
        "id": "c3d14d92-6e5d-4892-8007-b05d1fe98099",
        "title": "СДЭК расширяет сотрудничество с вузами и приглашает студентов на стажировки",
        "cover": {
            "type": "gallery",
            "images": [
                {
                    "s": "/assets/newsCover_1775212080-s.jpeg",
                    "m": "/assets/newsCover_1775212080-m.jpeg",
                    "l": "/assets/newsCover_1775212080-l.jpeg",
                    "hd": "/assets/newsCover_1775212080-hd.jpeg"
                },
                {
                    "s": "/assets/newsCover_1775211891-s.jpeg",
                    "m": "/assets/newsCover_1775211891-m.jpeg",
                    "l": "/assets/newsCover_1775211891-l.jpeg",
                    "hd": "/assets/newsCover_1775211891-hd.jpeg"
                }
            ]
        },
        "likeCount": 3,
        "viewCount": 95,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-04-03T10:25:52Z",
        "rubrics": [
            {"id": 2, "slug": "common", "name": "Наша жизнь"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    },
    {
        "id": "9c2273f6-9fa0-4f74-99ae-bdf663fb4613",
        "title": "Закрытие зимнего сезона с сообществом СДЭК Актив",
        "cover": {
            "type": "gallery",
            "images": [
                {
                    "s": "/assets/newsCover_1775025329-s.png",
                    "m": "/assets/newsCover_1775025329-m.png",
                    "l": "/assets/newsCover_1775025329-l.png",
                    "hd": "/assets/newsCover_1775025329-hd.png"
                },
                {
                    "s": "/assets/newsCover_1775025330-s.png",
                    "m": "/assets/newsCover_1775025330-m.png",
                    "l": "/assets/newsCover_1775025330-l.png",
                    "hd": "/assets/newsCover_1775025330-hd.png"
                },
                {
                    "s": "/assets/newsCover_1775025334-s.png",
                    "m": "/assets/newsCover_1775025334-m.png",
                    "l": "/assets/newsCover_1775025334-l.png",
                    "hd": "/assets/newsCover_1775025334-hd.png"
                },
                {
                    "s": "/assets/newsCover_1775025334-s.png",
                    "m": "/assets/newsCover_1775025334-m.png",
                    "l": "/assets/newsCover_1775025334-l.png",
                    "hd": "/assets/newsCover_1775025334-hd.png"
                }
            ]
        },
        "likeCount": 4,
        "viewCount": 39,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-04-02T11:21:52Z",
        "rubrics": [
            {"id": 12, "slug": "cdek-active", "name": "CDEK Актив"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    },
    {
        "id": "818b4ff7-09f0-453e-b8c8-1894aeb6887a",
        "title": "ИИ — это не магия, а полезный навык. Новый курс «Знакомство с нейросетями»",
        "cover": {
            "type": "gallery",
            "images": [
                {
                    "s": "/assets/newsCover_1774867719-s.png",
                    "m": "/assets/newsCover_1774867719-m.png",
                    "l": "/assets/newsCover_1774867719-l.png",
                    "hd": "/assets/newsCover_1774867719-hd.png"
                }
            ]
        },
        "likeCount": 5,
        "viewCount": 48,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-03-31T03:00:00Z",
        "rubrics": [
            {"id": 11, "slug": "school", "name": "CDEK Univer"},
            {"id": 10, "slug": "top", "name": "Важное для работы"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    },
    {
        "id": "96d1a8f8-8b09-4951-a018-bed5b32c77dc",
        "title": "Налоговые вычеты: краткая инструкция",
        "cover": {
            "type": "gallery",
            "images": [
                {
                    "s": "/assets/newsCover_1774780898-s.jpg",
                    "m": "/assets/newsCover_1774780898-m.jpg",
                    "l": "/assets/newsCover_1774780898-l.jpg",
                    "hd": "/assets/newsCover_1774780898-hd.jpg"
                }
            ]
        },
        "likeCount": 5,
        "viewCount": 148,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-03-29T10:42:22Z",
        "rubrics": [
            {"id": 2, "slug": "common", "name": "Наша жизнь"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    },
    {
        "id": "9edd1b7e-e3c3-4356-aea6-10d21ebfe248",
        "title": "Результаты кибертурнира и первые победы СДЭК на внешнем соревновании",
        "cover": {
            "type": "carousel",
            "images": [
                {
                    "s": "/assets/newsCover_1774612375-s.png",
                    "m": "/assets/newsCover_1774612375-m.png",
                    "l": "/assets/newsCover_1774612375-l.png",
                    "hd": "/assets/newsCover_1774612375-hd.png"
                }
            ]
        },
        "likeCount": 5,
        "viewCount": 154,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-03-27T12:01:00Z",
        "rubrics": [
            {"id": 2, "slug": "common", "name": "Наша жизнь"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    },
    {
        "id": "d4b99f7d-b389-491b-bb52-b5dd8e61d4c1",
        "title": "Новинки марта в программе корпоративных скидок BestBenefits",
        "cover": {
            "type": "carousel",
            "images": [
                {
                    "s": "/assets/newsCover_1774612312-s.png",
                    "m": "/assets/newsCover_1774612312-m.png",
                    "l": "/assets/newsCover_1774612312-l.png",
                    "hd": "/assets/newsCover_1774612312-hd.png"
                }
            ]
        },
        "likeCount": 3,
        "viewCount": 63,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-03-27T11:52:23Z",
        "rubrics": [
            {"id": 9, "slug": "skidki", "name": "Конкурсы, скидки, акции"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    },
    {
        "id": "10ec85b3-f7c5-49ea-bd80-b71e1d0e6bd6",
        "title": "Обзор коллекции SMART с победительницей эфира CDEK.FM",
        "cover": {
            "type": "gallery",
            "images": [
                {
                    "s": "/assets/newsCover_1774529096-s.jpeg",
                    "m": "/assets/newsCover_1774529096-m.jpeg",
                    "l": "/assets/newsCover_1774529096-l.jpeg",
                    "hd": "/assets/newsCover_1774529096-hd.jpeg"
                },
                {
                    "s": "/assets/newsCover_1774529377-s.jpeg",
                    "m": "/assets/newsCover_1774529377-m.jpeg",
                    "l": "/assets/newsCover_1774529377-l.jpeg",
                    "hd": "/assets/newsCover_1774529377-hd.jpeg"
                }
            ]
        },
        "likeCount": 7,
        "viewCount": 71,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-03-26T12:43:00Z",
        "rubrics": [
            {"id": 2, "slug": "common", "name": "Наша жизнь"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    },
    {
        "id": "ec25df32-70cd-4235-8950-a483363dc52d",
        "title": "Новое обучение от эксперта!",
        "cover": {
            "type": "gallery",
            "images": [
                {
                    "s": "/assets/newsCover_1774358706-s.png",
                    "m": "/assets/newsCover_1774358706-m.png",
                    "l": "/assets/newsCover_1774358706-l.png",
                    "hd": "/assets/newsCover_1774358706-hd.png"
                }
            ]
        },
        "likeCount": 5,
        "viewCount": 72,
        "isBreaking": False,
        "needConfirmation": False,
        "viewed": False,
        "isLiked": False,
        "publishedAt": "2026-03-24T13:28:00Z",
        "rubrics": [
            {"id": 11, "slug": "school", "name": "CDEK Univer"}
        ],
        "directions": [
            {"id": 3, "slug": "cdek", "name": "CDEK"}
        ],
        "isImportant": False
    }
]

MIN_DATE_PUBLICATION = "2025-01-31T08:03:00Z"

@app.route('/api/v1/news/feed/company/short', methods=['GET'])
def get_news_feed():
    per_page = request.args.get('perPage', default=10, type=int)
    page = request.args.get('page', default=1, type=int)
    
    if per_page > 100:
        per_page = 100
    
    total_pages = (len(ALL_NEWS) + per_page - 1) // per_page
    
    if page > total_pages:
        return jsonify({
            "totalPages": total_pages,
            "perPage": per_page,
            "news": [],
            "minDatePublication": MIN_DATE_PUBLICATION
        })
    
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_news = ALL_NEWS[start_index:end_index]
    
    return jsonify({
        "totalPages": total_pages,
        "perPage": per_page,
        "news": paginated_news,
        "minDatePublication": MIN_DATE_PUBLICATION
    })

@app.route('/api/v1/news/feed/company/empty', methods=['GET'])
def get_empty_news_feed():
    per_page = request.args.get('perPage', default=10, type=int)
    page = request.args.get('page', default=1, type=int)
    
    return jsonify({
        "totalPages": 0,
        "perPage": per_page,
        "news": [],
        "minDatePublication": MIN_DATE_PUBLICATION
    })

if __name__ == '__main__':
    print(f"Сервер запущен на http://localhost:5000")
    print(f"Статические файлы отдаются из папки: {ASSETS_DIR.absolute()}")
    print(f"Пример URL картинки: http://localhost:5000/assets/newsCover_1774529377-hd.jpeg")
    serve(app, host='0.0.0.0', port=5000)
