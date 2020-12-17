# Utilizing vrMessageService
def receivedMessage(message_id, args):
    messages = (
        'VRED_MSG_ARGV',
        'VRED_MSG_CHANGED_CAMERA_UP',
        'VRED_MSG_CHANGED_MATERIAL',
        'VRED_MSG_CHANGED_PB_PARAMETERS',
        'VRED_MSG_CHANGED_SCENEGRAPH',
        'VRED_MSG_CONVERT_OSF_FILE',
        'VRED_MSG_DESELECTED_NODE',
        'VRED_MSG_EXPORTED_FILE',
        'VRED_MSG_IDLE',
        'VRED_MSG_IMPORTED_FILE',
        'VRED_MSG_INIT',
        'VRED_MSG_KEY_PRESSED',
        'VRED_MSG_KEY_RELEASED',
        'VRED_MSG_LOADED_GEOMETRY',
        'VRED_MSG_LOOP',
        'VRED_MSG_NEW_SCENE',
        'VRED_MSG_NONE',
        'VRED_MSG_PRENEW_SCENE',
        'VRED_MSG_PRE_QUIT',
        'VRED_MSG_PROJECT',
        'VRED_MSG_PROJECT_LOADED',
        'VRED_MSG_PROJECT_MERGED',
        'VRED_MSG_SAVED_GEOMETRY',
        'VRED_MSG_SELECTED_CAMERA',
        'VRED_MSG_SELECTED_LIGHT',
        'VRED_MSG_SELECTED_MATERIAL',
        'VRED_MSG_SELECTED_NODE',
        'VRED_MSG_SWITCH_MATERIAL_CHANGED',
        'VRED_MSG_UPDATE_UI',
        'VRED_MSG_USER',
        )

    # Print the message that was signaled
    for message in messages:
        if message_id == getattr(vrController, message):
            print(message)

    # Listen specifically to the SELECTED CAMERA message
    if message_id == vrController.VRED_MSG_SELECTED_CAMERA:
        print("Camera selected!")

vrMessageService.message.connect(receivedMessage)