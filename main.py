from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

Glossary = {
    'Component-Based Architecture': 'A design approach where user interfaces are built using reusable and self-contained components, enabling scalability and modularity in UI libraries.',
    'Atomic Design': 'A methodology for crafting UI libraries that decompose interfaces into five distinct levels: atoms, molecules, organisms, templates, and pages.',
    'Design Tokens': 'Variables that store design decisions (e.g., colors, typography, spacing) to ensure consistent theming across components and platforms.',
    'Theming': 'The capability to customize the appearance of a UI library to match a corporate brand\'s identity, often achieved through design tokens and CSS variables.',
    'Accessibility (A11y)': 'Ensuring components are usable by individuals with disabilities, adhering to standards like WCAG to support inclusive design practices.',
    'Responsive Design': 'Designing components to adapt seamlessly to different screen sizes and orientations, ensuring usability across devices.',
    'State Management': 'Techniques and patterns for handling component states (e.g., loading, error, or success states) within a UI library to maintain predictable behavior.',
    'Style Guide': 'A comprehensive document or tool that outlines the visual and functional standards for components, serving as a reference for developers and designers.',
    'Storybook': 'A popular tool for developing, testing, and documenting UI components in isolation, aiding in the iterative design process.',
    'Component Testing': 'The practice of validating individual UI components for correctness, interactivity, and visual integrity using tools like Jest, React Testing Library, or Cypress.',
}

class CreateRequest(BaseModel):
    Concept: str
    Definition: str

class DefinitionResponse(BaseModel):
    Concept: str
    Definition: str

class BaseResponse(BaseModel):
    Status: int
    Message: str

class UpdateRequest(BaseModel):
    NewDefinition: str


@app.get('/about')
async def about():
    return {'about': 'This is a glosary. You can get, create and modify them'}

@app.get('/author')
async def author():
    return {'author': 'Karandasheva Nadya'}

@app.get('/all')
async def all():
    return JSONResponse(content=Glossary)

@app.get('/list')
async def list():
    responseDict = {}
    counter = 1
    for item in Glossary.keys():
        responseDict[counter] = item.capitalize()
        counter += 1
    return JSONResponse(content=responseDict)

@app.get('/definition/{definitionName}')
async def definition(definitionName: str):
    definitionName = definitionName.lower()
    definitionText = Glossary.get(definitionName)
    definitionName = definitionName.capitalize()
    return DefinitionResponse(
        Concept = definitionName,
        Definition = definitionText
    )

@app.post('/create')
async def create(request: CreateRequest):
    if (request.Concept.lower() in Glossary):
        return BaseResponse(
            Status = 406,
            Message = f'{request.Concept.capitalize()} already exists in dictionary. Use /update/{request.Concept.capitalize()} instead.'
        )
    else:
        Glossary[request.Concept.lower()] = request.Definition
        return BaseResponse(
            Status = 200,
            Message = f'Successfully added your definition of {request.Concept.capitalize()}'
        )

@app.delete('/remove/{definitionName}')
async def remove(definitionName: str):
    if (definitionName.lower() in Glossary):
        Glossary.pop(definitionName.lower())
        return BaseResponse(
            Status = 200,
            Message = f'{definitionName.capitalize()} successfully removed from glossary'
        )
    else:
        return BaseResponse(
            Status=404,
            Message=f'{definitionName.capitalize()} is not in the glossary.'
        )

# Обновление определения
@app.put('/update/{definitionName}')
async def update(request: UpdateRequest, definitionName: str):
    if (definitionName.lower() in Glossary):
        Glossary[definitionName.lower()] = request.NewDefinition
        return BaseResponse(
            Status = 200,
            Message = f'Successfully changed definition of {definitionName.capitalize()}'
        )
    else:
        return BaseResponse(
            Status=404,
            Message=f'{definitionName.capitalize()} does not exists in glossary.'
        )

