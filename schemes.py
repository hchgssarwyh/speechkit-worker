from typing import List, Any
from pydantic import BaseModel
from typing import Optional

class Alternative(BaseModel):
    words: List['Word']
    text: str
    startTimeMs: str
    endTimeMs: str
    confidence: int
    languages: List['Language']

    @classmethod
    def from_dict(cls, obj: Any) -> 'Alternative':
        return cls(
            words=[Word.from_dict(y) for y in obj.get("words", [])],
            text=str(obj.get("text", "")),
            startTimeMs=str(obj.get("startTimeMs", "")),
            endTimeMs=str(obj.get("endTimeMs", "")),
            confidence=int(obj.get("confidence", 0)),
            languages=[Language.from_dict(y) for y in obj.get("languages", [])]
        )

class AudioCursors(BaseModel):
    receivedDataMs: str
    resetTimeMs: str
    partialTimeMs: str
    finalTimeMs: str
    finalIndex: str
    eouTimeMs: str

    @classmethod
    def from_dict(cls, obj: Any) -> 'AudioCursors':
        return cls(
            receivedDataMs=str(obj.get("receivedDataMs", "")),
            resetTimeMs=str(obj.get("resetTimeMs", "")),
            partialTimeMs=str(obj.get("partialTimeMs", "")),
            finalTimeMs=str(obj.get("finalTimeMs", "")),
            finalIndex=str(obj.get("finalIndex", "")),
            eouTimeMs=str(obj.get("eouTimeMs", ""))
        )

class EouUpdate(BaseModel):
    timeMs: str

    @classmethod
    def from_dict(cls, obj: Any) -> 'EouUpdate':
        return cls(timeMs=str(obj.get("timeMs", "")))

class Final(BaseModel):
    alternatives: List[Alternative]
    channelTag: str

    @classmethod
    def from_dict(cls, obj: Any) -> 'Final':
        return cls(
            alternatives=[Alternative.from_dict(y) for y in obj.get("alternatives", [])],
            channelTag=str(obj.get("channelTag", ""))
        )

class FinalRefinement(BaseModel):
    finalIndex: str
    normalizedText: 'NormalizedText'

    @classmethod
    def from_dict(cls, obj: Any) -> 'FinalRefinement':
        return cls(
            finalIndex=str(obj.get("finalIndex", "")),
            normalizedText=NormalizedText.from_dict(obj.get("normalizedText", {}))
        )

class Language(BaseModel):
    languageCode: str
    probability: float

    @classmethod
    def from_dict(cls, obj: Any) -> 'Language':
        return cls(
            languageCode=str(obj.get("languageCode", "")),
            probability=float(obj.get("probability", 0.0))
        )

class LettersPerSecond(BaseModel):
    min: float
    max: float
    mean: float
    std: str
    quantiles: List['Quantile']

    @classmethod
    def from_dict(cls, obj: Any) -> 'LettersPerSecond':
        return cls(
            min=float(obj.get("min", 0.0)),
            max=float(obj.get("max", 0.0)),
            mean=float(obj.get("mean", 0.0)),
            std=str(obj.get("std", "")),
            quantiles=[Quantile.from_dict(y) for y in obj.get("quantiles", [])]
        )

class LettersPerUtterance(BaseModel):
    min: int
    max: int
    mean: int
    std: str
    quantiles: List['Quantile']

    @classmethod
    def from_dict(cls, obj: Any) -> 'LettersPerUtterance':
        return cls(
            min=int(obj.get("min", 0)),
            max=int(obj.get("max", 0)),
            mean=int(obj.get("mean", 0)),
            std=str(obj.get("std", "")),
            quantiles=[Quantile.from_dict(y) for y in obj.get("quantiles", [])]
        )

class NormalizedText(BaseModel):
    alternatives: List[Alternative]
    channelTag: str

    @classmethod
    def from_dict(cls, obj: Any) -> 'NormalizedText':
        return cls(
            alternatives=[Alternative.from_dict(y) for y in obj.get("alternatives", [])],
            channelTag=str(obj.get("channelTag", ""))
        )

class Quantile(BaseModel):
    level: float
    value: float

    @classmethod
    def from_dict(cls, obj: Any) -> 'Quantile':
        return cls(
            level=float(obj.get("level", 0.0)),
            value=float(obj.get("value", 0.0))
        )

class Result(BaseModel):
    sessionUuid: 'SessionUuid'
    audioCursors: AudioCursors
    responseWallTimeMs: str
    final: Final
    channelTag: str
    finalRefinement: FinalRefinement
    eouUpdate: EouUpdate
    speakerAnalysis: 'SpeakerAnalysis'

    @classmethod
    def from_dict(cls, obj: Any) -> 'Result':
        return cls(
            sessionUuid=SessionUuid.from_dict(obj.get("sessionUuid", {})),
            audioCursors=AudioCursors.from_dict(obj.get("audioCursors", {})),
            responseWallTimeMs=str(obj.get("responseWallTimeMs", "")),
            final=Final.from_dict(obj.get("final", {})),
            channelTag=str(obj.get("channelTag", "")),
            finalRefinement=FinalRefinement.from_dict(obj.get("finalRefinement", {})),
            eouUpdate=EouUpdate.from_dict(obj.get("eouUpdate", {})),
            speakerAnalysis=SpeakerAnalysis.from_dict(obj.get("speakerAnalysis", {}))
        )

class Root(BaseModel):
    result: Result

    @classmethod
    def from_dict(cls, obj: Any) -> 'Root':
        return cls(result=Result.from_dict(obj.get("result", {})))

class SessionUuid(BaseModel):
    uuid: str
    userRequestId: str

    @classmethod
    def from_dict(cls, obj: Any) -> 'SessionUuid':
        return cls(
            uuid=str(obj.get("uuid", "")),
            userRequestId=str(obj.get("userRequestId", ""))
        )

class SpeakerAnalysis(BaseModel):
    speakerTag: str
    windowType: str
    speechBoundaries: 'SpeechBoundaries'
    totalSpeechMs: str
    speechRatio: int
    totalSilenceMs: str
    silenceRatio: int
    wordsCount: str
    lettersCount: str
    wordsPerSecond: 'WordsPerSecond'
    lettersPerSecond: LettersPerSecond
    wordsPerUtterance: 'WordsPerUtterance'
    lettersPerUtterance: LettersPerUtterance
    utteranceCount: str
    utteranceDurationEstimation: 'UtteranceDurationEstimation'

    @classmethod
    def from_dict(cls, obj: Any) -> 'SpeakerAnalysis':
        return cls(
            speakerTag=str(obj.get("speakerTag", "")),
            windowType=str(obj.get("windowType", "")),
            speechBoundaries=SpeechBoundaries.from_dict(obj.get("speechBoundaries", {})),
            totalSpeechMs=str(obj.get("totalSpeechMs", "")),
            speechRatio=int(obj.get("speechRatio", 0)),
            totalSilenceMs=str(obj.get("totalSilenceMs", "")),
            silenceRatio=int(obj.get("silenceRatio", 0)),
            wordsCount=str(obj.get("wordsCount", "")),
            lettersCount=str(obj.get("lettersCount", "")),
            wordsPerSecond=WordsPerSecond.from_dict(obj.get("wordsPerSecond", {})),
            lettersPerSecond=LettersPerSecond.from_dict(obj.get("lettersPerSecond", {})),
            wordsPerUtterance=WordsPerUtterance.from_dict(obj.get("wordsPerUtterance", {})),
            lettersPerUtterance=LettersPerUtterance.from_dict(obj.get("lettersPerUtterance", {})),
            utteranceCount=str(obj.get("utteranceCount", "")),
            utteranceDurationEstimation=UtteranceDurationEstimation.from_dict(obj.get("utteranceDurationEstimation", {}))
        )

class SpeechBoundaries(BaseModel):
    startTimeMs: str
    endTimeMs: str

    @classmethod
    def from_dict(cls, obj: Any) -> 'SpeechBoundaries':
        return cls(
            startTimeMs=str(obj.get("startTimeMs", "")),
            endTimeMs=str(obj.get("endTimeMs", ""))
        )

class UtteranceDurationEstimation(BaseModel):
    min: int
    max: int
    mean: int
    std: str
    quantiles: List[Quantile]

    @classmethod
    def from_dict(cls, obj: Any) -> 'UtteranceDurationEstimation':
        return cls(
            min=int(obj.get("min", 0)),
            max=int(obj.get("max", 0)),
            mean=int(obj.get("mean", 0)),
            std=str(obj.get("std", "")),
            quantiles=[Quantile.from_dict(y) for y in obj.get("quantiles", [])]
        )

class Word(BaseModel):
    text: str
    startTimeMs: str
    endTimeMs: str

    @classmethod
    def from_dict(cls, obj: Any) -> 'Word':
        return cls(
            text=str(obj.get("text", "")),
            startTimeMs=str(obj.get("startTimeMs", "")),
            endTimeMs=str(obj.get("endTimeMs", ""))
        )

class WordsPerSecond(BaseModel):
    min: float
    max: float
    mean: float
    std: str
    quantiles: List[Quantile]

    @classmethod
    def from_dict(cls, obj: Any) -> 'WordsPerSecond':
        return cls(
            min=float(obj.get("min", 0.0)),
            max=float(obj.get("max", 0.0)),
            mean=float(obj.get("mean", 0.0)),
            std=str(obj.get("std", "")),
            quantiles=[Quantile.from_dict(y) for y in obj.get("quantiles", [])]
        )

class WordsPerUtterance(BaseModel):
    min: int
    max: int
    mean: int
    std: str
    quantiles: List[Quantile]

    @classmethod
    def from_dict(cls, obj: Any) -> 'WordsPerUtterance':
        return cls(
            min=int(obj.get("min", 0)),
            max=int(obj.get("max", 0)),
            mean=int(obj.get("mean", 0)),
            std=str(obj.get("std", "")),
            quantiles=[Quantile.from_dict(y) for y in obj.get("quantiles", [])]
        )
