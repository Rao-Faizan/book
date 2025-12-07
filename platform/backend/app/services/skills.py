from typing import Dict, Any

# Tool Implementations

def code_explainer(code_snippet: str) -> Dict[str, Any]:
    """
    Analyzes a code snippet and returns a structured explanation.
    In a real scenario, this might use AST parsing or a secondary LLM call.
    For this demo, we return a prompt-ready structure.
    """
    return {
        "analysis_type": "code_explanation",
        "language_detected": "python" if "def " in code_snippet else "cpp", # Naive detection
        "snippet_length": len(code_snippet),
        "instruction": "Explain this code line-by-line and estimate time complexity."
    }

def ros_command_lookup(topic: str) -> Dict[str, str]:
    """
    Looks up standard ROS 2 topics and returns their message types and usage.
    """
    topic_db = {
        "/cmd_vel": {"type": "geometry_msgs/Twist", "usage": "Velocity commands"},
        "/scan": {"type": "sensor_msgs/LaserScan", "usage": "Lidar data"},
        "/tf": {"type": "tf2_msgs/TFMessage", "usage": "Transform tree"},
        "/odom": {"type": "nav_msgs/Odometry", "usage": "Robot position/velocity"},
        "/rgb/image_raw": {"type": "sensor_msgs/Image", "usage": "Camera stream"},
    }
    
    return topic_db.get(topic, {"type": "unknown", "usage": "Topic not found in standard DB"})

# Gemini Tool Declarations

ros_tool_declaration = {
    "name": "ros_command_lookup",
    "description": "Look up standard ROS 2 topic message types and usage.",
    "parameters": {
        "type_": "OBJECT",
        "properties": {
            "topic": {
                "type_": "STRING",
                "description": "The ROS topic name (e.g., /cmd_vel)"
            }
        },
        "required": ["topic"]
    }
}

code_tool_declaration = {
    "name": "code_explainer",
    "description": "Analyze code snippets to provide explanations.",
    "parameters": {
        "type_": "OBJECT",
        "properties": {
            "code_snippet": {
                "type_": "STRING",
                "description": "The code block to analyze"
            }
        },
        "required": ["code_snippet"]
    }
}

tools_list = [ros_command_lookup, code_explainer]
