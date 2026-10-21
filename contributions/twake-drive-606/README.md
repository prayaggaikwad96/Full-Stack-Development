# Proposed fix for linagora/twake-drive-mobile#606

## Verified problem
The app's user-selected theme controls React Native content and the status bar, while Android's three-button navigation bar still follows the native `Theme.AppCompat.DayNight` system theme. Issue #606 documents a reproducible mismatch when the app is forced to dark while the OS is light.

## Proposed upstream change
Keep the fix scoped to the native Android theme resources. The current upstream `AppTheme` enables `android:enforceNavigationBarContrast`, which can apply a light navigation-bar scrim and dark buttons on Android 10+ when the app's selected theme differs from the system theme.

A focused fix should set the navigation-bar system UI appearance from the same active app scheme as `StatusBar`, or provide a small native bridge that applies `WindowInsetsControllerCompat.isAppearanceLightNavigationBars` whenever `useActiveColorScheme()` changes. Test both directions:
- System light + app dark => dark navigation-bar surface with light navigation buttons.
- System dark + app light => light navigation-bar surface with dark navigation buttons.

Do not disable contrast enforcement globally unless device/API testing proves this is needed; doing so can reduce contrast on other configurations.

## Validation required before upstream PR
- Android emulator with three-button navigation, API 30 or newer.
- Test system-light/app-dark and system-dark/app-light.
- Confirm gesture navigation remains unaffected.
- Run `npm run lint` and `npm run typecheck` if the JS/native bridge is changed, plus the Android build.
- Confirm the final upstream diff and CI results before marking ready for review.

## Status
This file is a staging note only. It does not modify the upstream repository and must not be submitted as the actual fix. The connected GitHub integration has read-only permission to `linagora/twake-drive-mobile` and does not expose a fork-creation action, so it cannot safely publish an upstream contribution from this account.
