from anakonda.anakonda import apiv1 as api

from .task import TaskResource

api.add_resource(TaskResource, "/tasks", methods=["GET", "POST"], endpoint="tasks")

api.add_resource(
    TaskResource,
    "/tasks/<string:task_id>",
    methods=["GET", "PATCH", "DELETE"],
    endpoint="task",
)
