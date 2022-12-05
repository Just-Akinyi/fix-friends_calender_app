from api.models.events import Event, EventSchema
from flask_restx import Namespace, Resource
from flask import request, jsonify, make_response


event_namespace = Namespace('user',
                            description='namespace for user\'s event')


@event_namespace.route('/event', strict_slashes=False)
class Events(Resource):

    def post(self):
        '''
        Create a new event
        '''
        try:
            data = request.get_json()
            event_schema = EventSchema()
            event = event_schema.load(data)
            result = event_schema.dump(event.create())
            return make_response(jsonify({'events': result}), 201)
        except Exception as e:
            return make_response(jsonify({'error': 'Invalid input'}), 422)


@event_namespace.route('/events/<int:event_id>', strict_slashes=False)
class GetUpdateDelete(Resource):

    def get(self, event_id):
        '''
        Retrieve an event by id
        '''
        get_event = Event.query.get_or_404(event_id)
        event_schema = EventSchema()
        event = event_schema.dump(get_event)
        return make_response(jsonify({'event': event}), 201)

    def put(self, event_id):
        '''
       Update an event with id
        '''
        data = request.get_json()
        get_event = Event.query.get_or_404(event_id)
        for key in data.keys():
            if key in ['title', 'description', 'location']:
                setattr(get_event, key, data[key])
            else:
                return make_response(jsonify({'error': 'Invalid input'}), 422)
        event_schema = EventSchema()
        event = event_schema.dump(get_event.create())
        return make_response(jsonify({'event': event}), 200)

    def delete(self, event_id):
        '''
        Delete an event with id
        '''
        get_event = Event.query.get_or_404(event_id)
        get_event.delete()
        return make_response('', 204)


@event_namespace.route('/<int:user_id>/events', strict_slashes=False)
class UserEvents(Resource):
    def get(self, user_id):
        '''
        Get all events by a specific user
        '''
        get_events = Event.query.filter_by(user_id=user_id).all()
        event_schema = EventSchema(many=True)
        events = event_schema.dump(get_events)
        return make_response(jsonify({'events': events}), 200)