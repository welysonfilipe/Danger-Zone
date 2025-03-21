from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(90, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(9):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                return list_bg
