from typing import Optional, List, Dict, Any
import openai
from app.core.config import get_settings

settings = get_settings()

class LLMService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    async def generate_response(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """
        OpenAI API를 사용하여 응답을 생성합니다.
        """
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API 요청 중 오류 발생: {str(e)}")
            return None

    async def process_calendar_input(
        self,
        user_input: str,
        context: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        사용자 입력을 처리하여 일정 정보를 추출합니다.
        """
        messages = [
            {"role": "system", "content": "당신은 일정 관리를 돕는 어시스턴트입니다."},
            {"role": "user", "content": f"다음 내용에서 일정 정보를 추출해주세요: {user_input}"}
        ]
        
        if context:
            messages.insert(1, {
                "role": "system",
                "content": f"참고할 컨텍스트 정보입니다: {' '.join(context)}"
            })

        response = await self.generate_response(messages)
        return {"raw_response": response} 