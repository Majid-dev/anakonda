from anakonda.config import Config

STATUS_MESSAGE = {
    100: "OK",
    101: "Method is not implemented",
    102: "Schema validation failed",
    103: "Schema instance error",
    104: "Invalid input provided",
    105: "Media type is not supported",
    106: "Database error",
    107: "Resource not found",
    108: "Runtime is not available",
    109: "Resource is not updateable",
}


def jsonify(state={}, metadata={}, status=200, code=100, heasers={}):
    resource = {}
    resource["result"] = state
    resource["metadata"] = metadata
    resource["status"] = {
        "code": code,
        "message": STATUS_MESSAGE[code] if Config.DEBUG else None,
    }
    return resource, status, heasers
