# Commands to test

## Key

  X: Has specific test which is passing
  F: Has a test in some form, for example in the setup
  S: Currently skipping the test due to a failure

  Empty boxes mean no test exists currently

## Commands

 [F] AuthenticateCommand
 [F] ChangeSessionIdCommand
 [X] ChangeSlotCommand
 [S] ClearInventoriesCommand - Seems to not work as expected, clears "Opened" inventories
 [X] GetCurrentLocationCommand
 [X] GetCurrentSlotCommand
 [S] GetEntitiesCommand
 [X] GetEntityHandlingEnabledCommand
 [X] GetGamemodeCommand
 [ ] GetInventoriesCommand
 [X] GetInventoryEnabledCommand
 [X] GetMaxChatMessageLengthCommand
 [X] GetOnlinePlayersCommand
 [X] GetOnlinePlayersWithUUIDCommand
 [X] GetPitchCommand
 [X] GetPlayerInventoryCommand
 [X] GetPlayersLatencyCommand
 [X] GetServerHostCommand
 [X] GetServerPortCommand
 [X] GetServerTPSCommand
 [X] GetTerrainEnabledCommand
 [X] GetTimestampCommand
 [X] GetUserUUIDCommand
 [X] GetUsernameCommand
 [X] GetWorldCommand
 [X] GetYawCommand
 [S] ClientIsMovingCommand
 [ ] CloseInventoryCommand
 [ ] CreativeDeleteCommand
 [ ] CreativeGiveCommand
 [ ] DigBlockCommand
 [ ] DisconnectAndExitCommand
 [ ] InteractEntityCommand
 [ ] LogDebugToConsoleCommand
 [ ] LogDebugToConsoleTranslatedCommand
 [ ] LogToConsoleCommand
 [ ] LogToConsoleTranslatedCommand
 [ ] LookAtLocationCommand
 [ ] MoveToLocationCommand
 [ ] ReconnectToTheServerCommand
 [ ] RespawnCommand
 [ ] RunScriptCommand
 [ ] SelectTradeCommand
 [ ] SendAnimationCommand
 [ ] SendEntityActionCommand
 [ ] SendPlaceBlockCommand
 [ ] SetSlotCommand
 [ ] SetTerrainEnabledCommand
 [ ] SneakCommand
 [ ] UpdateCommandBlockCommand
 [ ] UpdateSignCommand
 [ ] UseItemInHandCommand
 [ ] WindowActionCommand

## Future test improvements

 [ ] GetPlayerInventoryCommand: Test whether the inventory can be moved etc
