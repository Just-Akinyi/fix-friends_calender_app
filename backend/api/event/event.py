from flask_restx import Namespace, Resource



event_namespace = Namespace('Event', description ='namespace for user\'s event ' )


@event_namespace.route('/event')
class Event(Resource):
     
    
    def post(self):
        
        '''
        Create a new event
        '''
        pass
    
@event_namespace.route('/events/<int:event_id>')
class GetUpdateDelete(Resource):
     
    
    def get(self, event_id):
        
        '''
        Retrieve an event by id
        '''
        pass
    
        
    def put(self, event_id):
        '''
       Update an event with id
        '''
        pass
    
    def delete(self, event_id):
        '''
        Delete an event with id 
        '''
        pass
    
    
@event_namespace.route('/<int:user_id>/events')
class UserEvents(Resource):
    def get(self, user_id):
        
        '''
        Get all events by a specific user
        '''
        pass