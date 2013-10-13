var castingApp = angular.module('castingApp', [])

castingApp.controller('CharacterListCtrl', 
                      ['$scope', 'Character', function($scope, Character){
    $scope.characters = Character.query();
    $scope.orderPropr = 'order';
}]);

castingApp.controller("CharacterDetailCtrl",
                    ['$scope', '$characterParams', 'Character', 
                    function($scope, $characterParams, Character){
    $scope.character = Character.get({slug: $characterParams.slug}, 
                                      function(character){
        $scope.characterName = character.name;
    });
                    
}]);
