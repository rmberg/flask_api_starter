from flask import request
from flask_restful import Resource
from database import db
from models.widget import Widget, WidgetSchema

widgets_schema = WidgetSchema(many=True)
widget_schema = WidgetSchema()

class WidgetResource(Resource):

    def get(self):
        widgets = Widget.query.all()
        widgets = widgets_schema.dump(widgets).data
        return {'status': 'success', 'data': widgets}, 200

    def post(self):
        payload = request.get_json(force=True)

        if not payload:
            return {'message': 'No Input'}, 400

        data, errors = widget_schema.load(payload)

        if errors:
            return errors, 422

        widget = Widget(data['name'], data['price'])

        db.session.add(widget)
        db.session.commit()

        result = widget_schema.dump(widget).data

        return {'status': 'success', 'data': result}, 201