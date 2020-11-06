from blog.model.profile.profile_model import ProfileModel

import logging
logger = logging.getLogger(__name__)

class BlogManagment():

    def get_list_of_profiles():
        '''
            get_list_of_profiles : returns list of profile
        '''
        # fetching list of profile
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.error("This is an error message")
        return ProfileModel.get_list_of_profiles()


    def get_profile_by_id(id):
        '''
            get_list_of_profiles : returns list of profile

            Args:
                id: sad
        '''
        
        logger.debug("Fetching Profile by id - {id}".format(id=id))
        logger.info("Fetching Profile by id.")
        return ProfileModel.get_profile_by_id()